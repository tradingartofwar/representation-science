"""Two source-relative checks; never imported by the retained-only worker."""
import base64
import calendar
from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
from zoneinfo import ZoneInfo


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def utc_text(dt):
    return dt.isoformat().replace("+00:00", "Z")


def full_zone(reference):
    return ZoneInfo.from_file(io.BytesIO(base64.b64decode(reference["full_tzif_base64"])),
                              key=reference["scope"]["zone"])


def source_calendar(local, reference):
    """Read raw rule rows; use local-label cases, not T's UTC interval model."""
    wall = datetime.fromisoformat(local)
    active = []
    for row in reference["all_us_rule_rows"]:
        p = row.split()
        last = 9999 if p[3] == "max" else int(p[2] if p[3] == "only" else p[3])
        if int(p[2]) <= wall.year <= last:
            active.append(p)
    if active != [
        ["Rule", "US", "2007", "max", "-", "Mar", "Sun>=8", "2:00", "1:00", "D"],
        ["Rule", "US", "2007", "max", "-", "Nov", "Sun>=1", "2:00", "0", "S"]]:
        raise ValueError("reference source rule scope mismatch")
    if reference["new_york_zone_block"].strip().splitlines()[-1].split() != ["-5:00", "US", "E%sT"]:
        raise ValueError("reference zone source mismatch")
    sundays = lambda month: [week[6] for week in calendar.monthcalendar(wall.year, month) if week[6]]
    spring = datetime(wall.year, 3, sundays(3)[1], 2)
    autumn = datetime(wall.year, 11, sundays(11)[0], 2)
    if spring <= wall < spring + timedelta(hours=1):
        hours = []
    elif autumn - timedelta(hours=1) <= wall < autumn:
        hours = [4, 5]
    elif spring + timedelta(hours=1) <= wall < autumn - timedelta(hours=1):
        hours = [4]
    else:
        hours = [5]
    return sorted(utc_text((wall + timedelta(hours=h)).replace(tzinfo=timezone.utc)) for h in hours)


def forward_search(local, reference):
    """Search UTC minutes forwards, never assign a fold to the input label."""
    wall = datetime.fromisoformat(local)
    center = wall.replace(tzinfo=timezone.utc)
    zone = full_zone(reference)
    return [utc_text(utc) for minute in range(-1440, 1441)
            if (utc := center + timedelta(minutes=minute)).astimezone(zone).replace(tzinfo=None) == wall]


def truth(local, reference):
    a, b = forward_search(local, reference), source_calendar(local, reference)
    if a != b:
        raise RuntimeError(f"REFERENCE_CONFLICT {local}: {a!r} != {b!r}")
    return {"utc_candidates": a, "forward_search": a, "source_calendar": b, "agreement": True}


def evidence_valid(arm, payload, local, response, reference):
    evidence = response.get("evidence", {})
    if evidence.get("payload_sha256") != hashlib.sha256(canonical(payload).encode()).hexdigest():
        return False
    wall = datetime.fromisoformat(local)
    expected = []
    if arm == "B":
        if evidence.get("kind") != "fold-roundtrip":
            return False
        zone = full_zone(reference)
        # Check both the claimed inversion and each forward round trip.
        for fold in (0, 1):
            utc = wall.replace(tzinfo=zone, fold=fold).astimezone(timezone.utc)
            back = utc.astimezone(zone).replace(tzinfo=None)
            expected.append({"fold": fold, "utc": utc_text(utc),
                             "roundtrip_local": back.isoformat(), "accepted": back == wall})
    elif arm == "T":
        if evidence.get("kind") != "interval-preimages":
            return False
        for index, row in enumerate(payload["body"]["intervals"]):
            utc = wall.replace(tzinfo=timezone.utc) - timedelta(seconds=row["offset_seconds"])
            expected.append({"interval": index, "utc": utc_text(utc),
                             "accepted": row["start"] <= int(utc.timestamp()) < row["end_exclusive"]})
    else:
        return False
    return (canonical(evidence.get("trials")) == canonical(expected)
            and sorted({t["utc"] for t in expected if t["accepted"]}) == response["utc_candidates"])


def grade(arm, payload, local, response, reference, answer_key):
    result = {"verdict": "UNKNOWN", "reason": "UNSUPPORTED", "correct": None,
              "complete": None, "justified": False}
    if response.get("execution") != "ANSWER":
        return result
    expected = answer_key["utc_candidates"]
    got = response.get("utc_candidates")
    status = {0: "missing", 1: "unique", 2: "ambiguous"}[len(expected)]
    if got != expected or response.get("status") != status:
        valid_list = isinstance(got, list) and all(isinstance(x, str) for x in got)
        return {**result, "verdict": "INADEQUATE", "reason": "WRONG_OR_INCOMPLETE_ANSWER",
                "correct": valid_list and not (set(got) - set(expected)),
                "complete": valid_list and not (set(expected) - set(got)),
                "counterexample": {"expected": expected, "received": got,
                                   "expected_status": status, "received_status": response.get("status")}}
    result.update(correct=True, complete=True)
    if (response.get("local") != local or response.get("zone") != reference["scope"]["zone"]
            or response.get("source_archive_sha256") != reference["source"]["archive_sha256"]):
        return {**result, "reason": "IDENTITY_NOT_CERTIFIED"}
    try:
        justified = evidence_valid(arm, payload, local, response, reference)
    except (KeyError, TypeError, ValueError):
        justified = False
    return {**result, "verdict": "ADEQUATE" if justified else "UNKNOWN",
            "reason": "EXACT_SET_AND_EVIDENCE" if justified else "EVIDENCE_NOT_CERTIFIED",
            "justified": justified}
