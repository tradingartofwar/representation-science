"""Separately structured checker; imports no operational decoder code."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path


def load_audit():
    path=Path(__file__).resolve().parent.parent/'exp001_audit.py'
    spec=importlib.util.spec_from_file_location('audit_reference',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def reference(vs,z):
    a=load_audit()
    bands=a.safe_by_bands(vs,z)
    events=a.safe_by_events(vs,z)
    if bands!=events:
        raise ArithmeticError('reference methods disagree')
    optimum,times,candidate_count=a.optimize_by_tents(vs)
    return dict(exists=bool(bands),optimum=optimum,times=times,components=bands,
                verification_work=dict(complete_set_methods=2,optimization_candidates=candidate_count,
                    unique_threshold_events=len({F(0),F(1)}|{t for v in vs for k in range(v)
                                                           for t in ((k+z)/v,(k+1-z)/v)})),
                verification='band intersection, independent threshold-event decomposition and tent crossings')


def contains(parts,t):
    return any(a<=t<=b for a,b in parts)


def set_difference_witness(expected,received):
    events=sorted({t for parts in (expected,received) for pair in parts for t in pair})
    probes=sorted(set(events)|{(a+b)/2 for a,b in zip(events,events[1:])})
    for t in probes:
        left,right=contains(expected,t),contains(received,t)
        if left!=right:
            return dict(time=str(t),expected_safe=left,received_safe=right)
    return None


def grade(question,response,truth,vs,z):
    out=response.get('output')
    result=dict(status='UNKNOWN',reason=response.get('reason',''),counterexample=None)
    if response.get('resource_limit'):
        result['reason']='resource limit; no insufficiency inference'
        return result
    if response.get('exhausted'):
        result.update(status='INADEQUATE',reason='declared carrier exhausted while physical witness exists',
                      counterexample=dict(reference_witness=str(truth['components'][0][0])))
        return result
    if out is None:
        return result
    if question=='Q1':
        correct=out==truth['exists'] and isinstance(out,bool)
        evidence=dict(expected=truth['exists'],received=out)
    elif question=='Q2':
        t=F(out['time'])
        expected_laps=[(v*t).numerator//(v*t).denominator for v in vs]
        expected_phases=[v*t-lap for v,lap in zip(vs,expected_laps)]
        correct=(F(0)<=t<F(1) and out['laps']==expected_laps
                 and list(map(F,out['phases']))==expected_phases
                 and all(z<=p<=1-z for p in expected_phases))
        evidence=dict(time=str(t),direct_phase_lap_check=correct)
    elif question=='Q3':
        correct=F(out)==truth['optimum']
        evidence=dict(expected=str(truth['optimum']),received=out)
    elif question=='Q4':
        parsed=list(map(F,out))
        correct=parsed==truth['times']
        missing=sorted(set(truth['times'])-set(parsed))
        extra=sorted(set(parsed)-set(truth['times']))
        evidence=dict(missing_times=list(map(str,missing)),extra_times=list(map(str,extra)))
    elif question=='Q5':
        parsed=[tuple(map(F,p)) for p in out]
        # Canonical sorted disjoint closed components required; exact equality
        # verifies completeness, and event-based set difference gives a witness.
        correct=parsed==truth['components']
        evidence=set_difference_witness(truth['components'],parsed)
        if not correct and evidence is None:
            evidence=dict(reason='set equivalent but not canonical output grammar')
    else:
        raise ValueError(question)
    result['output_matches_reference']=correct
    if correct and response.get('supported'):
        result['status']='ADEQUATE'
        result['verification']=evidence
    elif not correct:
        result['status']='INADEQUATE'
        result['counterexample']=evidence
    else:
        result['reason']='correct output but declared decoder lacks global/completeness support'
        result['verification']=evidence
    return result
