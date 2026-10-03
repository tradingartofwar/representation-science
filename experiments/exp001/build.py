"""Build declared retained payloads. Does not score any candidate/query cell."""
import argparse
import hashlib
import json
from pathlib import Path
from core import F, Meter, physical_profile, serialize

SOURCE_COMMIT='f2126bfe929aae4eda77b4ea3418a4c38b47f0f5'
SOURCE_PATH='reviews/2026-09-29-cc-six-seven-transfer/verification.json'
SOURCE_BLOB='7588da7b71be67dd65fa39f13aba829e3ee1c85c'


def dump(path,obj):
    path.write_text(json.dumps(serialize(obj),indent=2,sort_keys=True)+'\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    raw=(args.source_root/SOURCE_PATH).read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if actual!=SOURCE_BLOB:
        raise ValueError('source blob does not match freeze basis')
    source=json.loads(raw)
    case=next(x for x in source['physical_controls'] if x['q']==10)
    rows=source['rows'][:6]
    # Source rows may be serialized integers; leave them exact.
    rows=[[int(a),int(b)] for a,b in rows]
    by_n={x['coordinates']:x for x in case['optimization']}
    def cache(n):
        return dict(kind='optimizer_cache',epoch='child' if n==7 else 'parent',
                    optimum=by_n[n]['maximum'],times=by_n[n]['all_maximizing_times'])
    parent_cache,child_cache=cache(6),cache(7)
    segments=dict(kind='segments',epoch='parent',q=10,rows=rows,
                  segments=[dict(lo='1/8',hi='5/24',c='7/8',d='3',
                                 parent=1,labels=[0,0,0,0,0,1]),
                            dict(lo='3/8',hi='1/2',c='9/8',d='2',
                                 parent=3,labels=[0,0,0,1,1,1])])
    edge_cells=[dict(vertices=c['vertices'],edges=c['edges'],labels=c['labels'])
                for c in source['parents']]
    edges=dict(kind='edges',epoch='parent',q=10,rows=rows,cells=edge_cells,
               convex_parent_semantics=True)
    facets=dict(kind='facets',epoch='parent',q=10,rows=rows,
                labels=[c['labels'] for c in source['parents']],
                cells=[[list(n)+[d] for name,n,d in c['constraints']]
                       for c in source['parents']])
    sets={epoch:dict(kind='threshold_set',epoch=epoch,threshold='1/8',
                    components=case[prefix+'_safe_components_at_1_over_8'])
          for epoch,prefix in [('parent','six'),('child','seven')]}
    profiles={}; counters={}
    for epoch,vs in [('parent',case['speeds'][:-1]),('child',case['speeds'])]:
        meter=Meter()
        profiles[epoch]=dict(kind='profile',epoch=epoch,speeds=vs,
                             pieces=physical_profile(vs,meter))
        counters[epoch]=dict(meter.counts)
    payloads={
        'R1':dict(static=dict(kind='scalar',epoch='child',optimum=by_n[7]['maximum']),
                  transfer=dict(kind='scalar',epoch='parent',optimum=by_n[6]['maximum'])),
        'R2':dict(static=parent_cache,transfer=parent_cache),
        'R3':dict(static=segments,transfer=segments),
        'R4':dict(static=edges,transfer=edges),
        'R5':dict(static=facets,transfer=facets),
        'R6':dict(static=profiles['child'],transfer=profiles['parent']),
        'C1':dict(static=sets['child'],transfer=sets['parent']),
        'C2':dict(static=child_cache,transfer=parent_cache),
    }
    args.output_dir.mkdir(parents=True,exist_ok=True)
    dump(args.output_dir/'payloads.json',payloads)
    dump(args.output_dir/'recovery_model.json',dict(kind='physical_generator',
         epoch='child',speeds=case['speeds']))
    dump(args.output_dir/'construction.json',dict(source_commit=SOURCE_COMMIT,
         source_path=SOURCE_PATH,source_git_blob=SOURCE_BLOB,
         work='Select pinned parent geometry/cache/set fields; construct R6 profiles from speeds',
         profile_construction_named_operations=counters,
         inherited_geometry_and_cache_construction_cost='UNMEASURED; not free or zero',
         segment_source='notes/CC_BOUNDED_SELECTOR_2026_09_29.md',
         segment_source_blob='c60878a2be02629d00cb867000ef7aa0d2fd2ab5',
         shared_generator_formula_only_in_rows_R3_R4_R5=True,
         static_source_epochs={k:v['static']['epoch'] for k,v in payloads.items()},
         transfer_all_parent_epochs=True))
    print(json.dumps({'payload_construction':'complete','matrix_scored':False}))


if __name__=='__main__':
    main()
