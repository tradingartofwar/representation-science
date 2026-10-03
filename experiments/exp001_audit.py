#!/usr/bin/env python3
"""Exact EXP-001 preflight, not a representation adequacy-matrix runner.

Standard-library only. Independently written from the pinned prose specification.
Band intersection and threshold-event decomposition check complete closed sets.
Tent-piece crossings determine the optimum without importing laboratory code.
Optional --source-root compares results with the pinned laboratory certificate.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json


def distance(v, t):
    phase = v * t % 1
    return min(phase, 1 - phase)


def separation(vs, t):
    return min(distance(v, t) for v in vs)


def merge(parts):
    out = []
    for a, b in sorted(parts):
        if out and a <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return out


def safe_by_bands(vs, z):
    parts = [(F(0), F(1))]
    for v in vs:
        bands = [((k + z) / v, (k + 1 - z) / v) for k in range(v)]
        parts = merge([(max(a, c), min(b, d)) for a, b in parts
                       for c, d in bands if max(a, c) <= min(b, d)])
    return parts


def safe_by_events(vs, z):
    # No intersection iteration: truth is constant between consecutive events.
    events = {F(0), F(1)}
    for v in vs:
        for k in range(v):
            events.update(((k + z) / v, (k + 1 - z) / v))
    events = sorted(events)
    parts = [(t, t) for t in events if separation(vs, t) >= z]
    for a, b in zip(events, events[1:]):
        if separation(vs, (a + b) / 2) >= z:
            # The predicate is closed; both endpoints must also satisfy it.
            assert separation(vs, a) >= z and separation(vs, b) >= z
            parts.append((a, b))
    return merge(parts)


def optimize_by_tents(vs):
    # All tents are affine between adjacent wrap/half-wrap events. The lower
    # envelope can change slope only at those events or a pairwise crossing.
    breaks = sorted({F(k, 2 * v) for v in vs for k in range(2 * v + 1)})
    candidates = set(breaks)
    for a, b in zip(breaks, breaks[1:]):
        mid = (a + b) / 2
        lines = []
        for v in vs:
            k = (v * mid).numerator // (v * mid).denominator
            if v * mid - k < F(1, 2):
                lines.append((v, -k))
            else:
                lines.append((-v, k + 1))
        for (s, c), (r, d) in combinations(lines, 2):
            if s != r:
                t = F(d - c, s - r)
                if a <= t <= b:
                    candidates.add(t)
    z = max(separation(vs, t) for t in candidates)
    points = sorted(t for t in candidates if separation(vs, t) == z)
    # Nonzero slopes preclude a positive-width constant maximum. Also check
    # that two differently structured complete-superlevel algorithms agree.
    peak_set = safe_by_bands(vs, z)
    assert peak_set == safe_by_events(vs, z) == [(t, t) for t in points]
    return z, points, len(candidates)


def serialize(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {str(k): serialize(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serialize(v) for v in x]
    return x


def audit():
    results = {}
    for name, vs in [('parent', (1, 10, 11, 12, 13, 23)),
                     ('child', (1, 10, 11, 12, 13, 23, 25))]:
        parts = safe_by_bands(vs, F(1, 8))
        assert parts == safe_by_events(vs, F(1, 8))
        z, points, count = optimize_by_tents(vs)
        results[name] = dict(speeds=vs, optimum=z, maximizers=points,
                             safe_set=parts, components=len(parts),
                             singleton_components=sum(a == b for a, b in parts),
                             tent_candidates=count,
                             total_safe_duration=sum(b-a for a,b in parts))
    child = results['child']
    assert child['optimum'] == F(1, 7)
    assert child['maximizers'] == [F(1,7),F(2,7),F(3,7),F(17,35),
                                  F(18,35),F(4,7),F(5,7),F(6,7)]
    assert results['parent']['optimum'] == F(4, 25)
    assert results['parent']['maximizers'] == [F(8,25), F(17,25)]
    assert all(distance(25, t) == 0 for t in results['parent']['maximizers'])
    witness = F(15,104)  # Independently apply the pinned E1 rounding at q=10.
    vs = child['speeds']
    laps = [int(v * witness) for v in vs]
    phases = [v * witness - lap for v, lap in zip(vs, laps)]
    assert separation(vs, witness) == F(1,8)
    assert witness not in child['maximizers']
    results['selector_witness'] = dict(time=witness, laps=laps, phases=phases)
    assert tuple((lap+phase)/witness for lap,phase in zip(laps,phases)) == vs
    results['q2_reconstructs_speeds'] = [(lap+phase)/witness
                                         for lap,phase in zip(laps,phases)]
    results['positive_components_without_maximizer'] = [
        (a,b) for a,b in child['safe_set'] if a<b
        and not any(a<=t<=b for t in child['maximizers'])]
    assert len(results['positive_components_without_maximizer']) == 2
    nonmax=F(17,36)
    assert separation(vs,nonmax)==F(5,36)<child['optimum']
    results['nonmaximizing_safe_interior_witness']=dict(time=nonmax,separation=F(5,36))
    # The missed old-edge point is retained by the convex hull of labelled
    # parent vertices. These coordinates are inspected pinned source data.
    p7_vertices=[(F(11,24),F(7,8),F(1,8)),
                 (F(1,2),F(13,16),F(1,8)),
                 (F(1,2),F(5,6),F(1,6)),
                 (F(1,2),F(7,8),F(1,8))]
    weights=[F(12,35),F(0),F(3,7),F(8,35)]
    recovered=tuple(sum(w*p[i] for w,p in zip(weights,p7_vertices))
                    for i in range(3))
    assert sum(weights)==1 and all(w>=0 for w in weights)
    assert recovered == (F(17,35),F(6,7),F(1,7))
    rows=[(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]
    labels=[0,0,1,1,2,3]
    x,y,z=recovered
    phases_p7=[a*x+b*y-m for (a,b),m in zip(rows,labels)]
    assert all(z<=p<=1-z for p in phases_p7)
    assert [(i,side) for i,p in enumerate(phases_p7)
            for side,v in [('lower',z),('upper',1-z)] if p==v] == [(1,'upper')]
    assert x<F(1,2) and z>F(1,8) and 10*x-y==4
    assert 5*x+2*y-z==4
    results['r4_internal_hull_recovery'] = dict(
        parent=7, vertices=p7_vertices, weights=weights, recovered=recovered,
        active_parent_band='y+z=1', new_band='5x+2y-z=4')
    # Founding record counterchecks, outside the EXP-001 candidate matrix.
    rank3 = (1,4,5,6,7,11,14,35,13)
    isolated = safe_by_bands(rank3,F(1,8))
    assert isolated == safe_by_events(rank3,F(1,8))
    assert isolated == [(F(i,8),F(i,8)) for i in (1,3,5,7)]
    sheet_case=(1,2,3,4,5,7,10,19,40)
    assert separation(sheet_case,F(25,152)) == F(1,8)
    assert all(distance(40,t)==0 for t in (F(1,8),F(7,40),F(3,8)))
    results['founding_record_counterchecks'] = dict(
        rr002_safe_set=isolated, rr003_witness=F(25,152),
        rr003_separation=separation(sheet_case,F(25,152)))
    # Nonphysical marginal-pair false positive from RR-LR-001.
    section = [(F(17,56),F(3,14)),(F(5,16),F(1,4))]
    assert all(4*x-y==1 for x,y in section)
    s_range=sorted(5*x+2*y for x,y in section)
    assert s_range==[F(109,56),F(33,16)]
    assert F(15,8)<s_range[0]<=s_range[1]<F(17,8)
    results['founding_record_counterchecks']['rr001_conditional_S']=s_range
    return results


def compare_pinned_source(root, results):
    pins = {
        'reviews/2026-09-29-cc-six-seven-transfer/verification.json':
            '7588da7b71be67dd65fa39f13aba829e3ee1c85c',
        'reviews/2026-09-29-cc-six-seven-transfer/countercheck.json':
            'cade5c407a63c2cd4c03f55559eb40a4b5dd686f',
        'reviews/2026-09-30-cc-three-parameter/summary.json':
            '2d9097aaa9a0c71de726ca73d8438452b6525f72',
        'reviews/2026-10-02-cc-sheet-coverage/run/SUMMARY.json':
            '64cfb9df716de9333ac8fadfa7b81bb725e6caea',
        'reviews/2026-10-02-cc-orbit-intervals/run/SUMMARY.json':
            'fa691c05e0d6812cdf9256ee2952ba5647d0a292',
    }
    docs = []
    for path, expected in pins.items():
        raw = (root/path).read_bytes()
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert blob == expected, (path, blob, expected)
        docs.append(json.loads(raw))
    primary, counter, rank3, sheets, orbit = docs
    q10 = next(c for c in primary['physical_controls'] if c['q']==10)
    for name, prefix, n in [('parent','six',6),('child','seven',7)]:
        computed = results[name]
        assert computed['safe_set']==q10[prefix+'_safe_components_at_1_over_8']
        for archived in (q10['optimization'], counter['physical']):
            record=next(c for c in archived if c['coordinates']==n
                        and c.get('q',10)==10)
            assert computed['optimum']==record['maximum']
            assert computed['maximizers']==record['all_maximizing_times']
    assert results['r4_internal_hull_recovery']['vertices']==primary['parents'][7]['vertices']
    assert rank3['classes']['sheets']['train']['menu_hits']==89
    assert rank3['classes']['sheets']['holdout']['menu_hits']==310
    assert rank3['classes']['sheets']['holdout']['class_hits']==318
    assert sheets['coverage']['full36']==643
    assert orbit['coverage']=={'all_components':1197,'positive_only':1196,'widest':981}
    assert orbit['misses']['positive_only']==[[1,4,13]]
    return dict(commit='f2126bfe929aae4eda77b4ea3418a4c38b47f0f5',
                verified_git_blobs=pins, q10_complete_sets_and_optima_match=True,
                founding_counts_match_stored_summaries=True,
                limit='Stored count reconciliation; large historical studies not rerun')


def main():
    if not __debug__:
        raise RuntimeError('Run with assertions enabled; do not use python -O')
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--source-root', type=Path)
    args = parser.parse_args()
    result = serialize(audit())
    if args.source_root:
        result['source_comparison']=compare_pinned_source(args.source_root,result)
    result['scope'] = 'Pre-execution geometry audit; no adequacy matrix scored'
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rendered = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end='')


if __name__ == '__main__':
    main()
