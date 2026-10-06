#!/usr/bin/env python3
"""One retained-only query. No reference/manifest/case-list/source file access."""
import time
START = time.perf_counter()
import base64
from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
import resource
import sys
from zoneinfo import ZoneInfo

DENIED = []


def audit(event, args):
    if event == "open" or event in {"os.listdir", "os.scandir", "os.system"} or event.startswith(("socket.", "subprocess.")):
        DENIED.append(event)
        raise PermissionError("retained-only worker forbids post-import source/OS access")


sys.addaudithook(audit)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def utc_text(dt):
    return dt.isoformat().replace("+00:00", "Z")


def solve(arm, payload, request):
    text = request["local"]
    wall = datetime.fromisoformat(text)
    scope = payload["scope"]
    if (wall.tzinfo is not None or wall.isoformat() != text or wall.second or wall.microsecond
            or not datetime.fromisoformat(scope["local_start"]) <= wall < datetime.fromisoformat(scope["local_end_exclusive"])):
        return {"execution": "UNSUPPORTED", "reason": "outside declared minute-grid domain", "local": text}
    found, trials = set(), []
    if arm == "B" and payload["body"]["format"] == "TZif":
        zone = ZoneInfo.from_file(io.BytesIO(base64.b64decode(payload["body"]["base64"], validate=True)), key=scope["zone"])
        for fold in (0, 1):
            utc = wall.replace(tzinfo=zone, fold=fold).astimezone(timezone.utc)
            back = utc.astimezone(zone).replace(tzinfo=None)
            accepted = back == wall
            trials.append({"fold": fold, "utc": utc_text(utc), "roundtrip_local": back.isoformat(), "accepted": accepted})
            if accepted:
                found.add(utc_text(utc))
        kind = "fold-roundtrip"
    elif arm == "T" and payload["body"]["format"] == "utc-offset-intervals":
        for index, row in enumerate(payload["body"]["intervals"]):
            utc = wall.replace(tzinfo=timezone.utc) - timedelta(seconds=row["offset_seconds"])
            accepted = row["start"] <= int(utc.timestamp()) < row["end_exclusive"]
            trials.append({"interval": index, "utc": utc_text(utc), "accepted": accepted})
            if accepted:
                found.add(utc_text(utc))
        kind = "interval-preimages"
    else:
        raise ValueError("unsupported arm/payload format")
    answers = sorted(found)
    return {"execution": "ANSWER", "local": text, "zone": scope["zone"],
            "source_archive_sha256": payload["source"]["archive_sha256"],
            "utc_candidates": answers, "status": {0: "missing", 1: "unique", 2: "ambiguous"}[len(answers)],
            "evidence": {"kind": kind, "payload_sha256": hashlib.sha256(canonical(payload).encode()).hexdigest(), "trials": trials}}


try:
    raw = sys.stdin.buffer.read(16385)
    if len(raw) > 16384:
        raise ValueError("request budget exceeded")
    msg = json.loads(raw)
    response = solve(msg["arm"], msg["payload"], msg["request"])
    result = {"response": response, "access": {"external_source_reads": 0, "denied_events": DENIED},
              "metrics": {"worker_seconds": time.perf_counter() - START,
                          "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}}
    encoded = canonical(result).encode()
    if len(encoded) > 16384:
        raise ValueError("response budget exceeded")
    sys.stdout.buffer.write(encoded + b"\n")
except Exception as exc:
    sys.stdout.write(canonical({"error": type(exc).__name__, "message": str(exc), "denied_events": DENIED}) + "\n")
    sys.exit(2)
