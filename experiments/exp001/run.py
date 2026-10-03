"""Run frozen operational comparison with isolated one-query subprocesses."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import traceback
from fractions import Fraction as F
from check import reference,grade

HERE=Path(__file__).resolve().parent
RUN_OUT=None


def compact(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def numeric_metrics(x):
    values=[]
    def visit(v):
        if isinstance(v,bool):
            return
        if isinstance(v,(str,int)):
            try:
                values.append(F(v))
            except ValueError:
                pass
        elif isinstance(v,list):
            for a in v: visit(a)
        elif isinstance(v,dict):
            for a in v.values(): visit(a)
    visit(x)
    return dict(numeric_fields=len(values),numerator_bits=sum(abs(v.numerator).bit_length() for v in values),
                denominator_bits=sum(v.denominator.bit_length() for v in values),
                max_integer_bits=max([0]+[max(abs(v.numerator).bit_length(),v.denominator.bit_length()) for v in values]))


def object_metrics(p):
    info=dict(kind=p['kind'],epoch=p['epoch'])
    for key in ('times','segments','pieces','components','speeds','rows'):
        if key in p: info[key]=len(p[key])
    if p['kind']=='edges':
        info.update(parents=len(p['cells']),edge_occurrences=sum(len(c['edges']) for c in p['cells']),
                    vertex_occurrences=sum(len(c['vertices']) for c in p['cells']))
    if p['kind']=='facets':
        info.update(parents=len(p['cells']),inequality_occurrences=sum(len(c) for c in p['cells']))
    if p['kind']=='threshold_set':
        info['singleton_components']=sum(a==b for a,b in p['components'])
    return info


def invoke(payload,question,mode,config):
    request=dict(payload=payload,question=question,mode=mode,
                 added_speed=config['added_speed'],threshold=config['threshold'])
    with tempfile.TemporaryDirectory(prefix='exp001-query-') as td:
        for name in ('core.py','worker.py'):
            shutil.copyfile(HERE/name,Path(td)/name)
        try:
            process=subprocess.run([sys.executable,'-s','worker.py'],input=compact(request),
                       text=True,capture_output=True,cwd=td,
                       env={'PATH':os.defpath,'PYTHONHASHSEED':'0','PYTHONDONTWRITEBYTECODE':'1'},
                       timeout=30)
        except subprocess.TimeoutExpired:
            return dict(supported=False,resource_limit='30-second process timeout',reason='resource limit')
        if process.returncode:
            raise RuntimeError(process.stderr)
        return json.loads(process.stdout)


def main():
    global RUN_OUT
    if not __debug__:
        raise RuntimeError('assertions must remain enabled')
    parser=argparse.ArgumentParser()
    parser.add_argument('--freeze-commit',required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    manifest=json.loads((HERE/'MANIFEST.json').read_text())
    for path,expected in manifest['sha256'].items():
        if sha(HERE/path)!=expected:
            raise ValueError('frozen input mismatch: '+path)
    config=json.loads((HERE/'config.json').read_text())
    payloads=json.loads((HERE/'payloads.json').read_text())
    recovery=json.loads((HERE/'recovery_model.json').read_text())
    args.output_dir.mkdir(parents=True,exist_ok=False)
    RUN_OUT=args.output_dir
    # All retained-only responses are sealed before any grade or recovery.
    responses=[]
    for row in config['rows']:
        for workload in ('static','transfer'):
            for question in config['questions']:
                for mode in ('native','internal'):
                    record=dict(row=row,workload=workload,question=question,mode=mode)
                    record['response']=invoke(payloads[row][workload],question,mode,config)
                    responses.append(record)
                    (args.output_dir/'RESPONSES.json').write_text(json.dumps(responses,indent=2,sort_keys=True)+'\n')
    (args.output_dir/'RESPONSES.json').write_text(json.dumps(responses,indent=2,sort_keys=True)+'\n')
    vs=recovery['speeds']; z=F(config['threshold'])
    truth=reference(vs,z)
    cells=[]
    for record in responses:
        item=dict(record)
        item['grade']=grade(item['question'],item['response'],truth,vs,z)
        item['output_bytes']=len(compact(item['response'].get('output')).encode())
        cells.append(item)
    # Reopening is separately invoked, never fed back into a retained-only run.
    recoveries=[]
    for row in config['rows']:
        for workload in ('static','transfer'):
            for question in config['questions']:
                relevant=[c for c in cells if c['row']==row and c['workload']==workload and c['question']==question]
                if all(c['grade']['status']=='ADEQUATE' for c in relevant):
                    continue
                response=invoke(recovery,question,'internal',config)
                checked=grade(question,response,truth,vs,z)
                rec=dict(row=row,workload=workload,question=question,response=response,grade=checked,
                         recovery_source='recovery_model.json',source_sha256=sha(HERE/'recovery_model.json'),
                         source_bytes=len(compact(recovery).encode()))
                recoveries.append(rec)
                for c in relevant:
                    c['after_source_recovery']='RECOVERABLE' if checked['status']=='ADEQUATE' else checked['status']
    metrics={row:{workload:dict(payload_bytes=len(compact(p).encode()),**numeric_metrics(p),objects=object_metrics(p))
                  for workload,p in entry.items()} for row,entry in payloads.items()}
    result=dict(freeze_commit=args.freeze_commit,manifest_sha256=sha(HERE/'MANIFEST.json'),
                scope='known q=10 development case; two declared decoder modes; no information-theoretic lower bound',
                cells=cells,recoveries=recoveries,payload_metrics=metrics,
                common_code_bytes={f:(HERE/f).stat().st_size for f in ('core.py','worker.py','check.py','run.py')},
                reference={k: str(v) if isinstance(v,F) else v for k,v in truth.items()})
    def convert(v):
        if isinstance(v,F): return str(v)
        if isinstance(v,dict): return {k:convert(a) for k,a in v.items()}
        if isinstance(v,(list,tuple)): return [convert(a) for a in v]
        return v
    (args.output_dir/'RESULTS.json').write_text(json.dumps(convert(result),indent=2,sort_keys=True)+'\n')
    summary={}
    for workload in ('static','transfer'):
        summary[workload]={mode:{row:{c['question']:c['grade']['status'] for c in cells
                                      if c['row']==row and c['workload']==workload and c['mode']==mode}
                                for row in config['rows']} for mode in ('native','internal')}
    summary['counts']=dict(retained_only_queries=len(cells),source_recovery_queries=len(recoveries),
                           adequate=sum(c['grade']['status']=='ADEQUATE' for c in cells),
                           inadequate=sum(c['grade']['status']=='INADEQUATE' for c in cells),
                           unknown=sum(c['grade']['status']=='UNKNOWN' for c in cells),
                           recovery_passes=sum(c['grade']['status']=='ADEQUATE' for c in recoveries))
    (args.output_dir/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))


if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        if RUN_OUT is not None:
            (RUN_OUT/'FAILURE.json').write_text(json.dumps(dict(status='STOPPED_NO_RETUNING',
                error=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()),indent=2)+'\n')
        raise
