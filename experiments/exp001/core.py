"""Exact operational decoders. No repository access or answer-key imports."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import ceil, floor


class BudgetExceeded(Exception):
    pass


class Meter:
    def __init__(self):
        self.counts = Counter()
        self.peak_pieces = 0

    def tick(self, kind, n=1):
        self.counts[kind] += n
        if sum(self.counts.values()) > 2000000:
            raise BudgetExceeded('two-million named operations')

    def pieces(self, items):
        self.peak_pieces = max(self.peak_pieces, len(items))
        if len(items) > 100000:
            raise BudgetExceeded('100000 profile pieces')
        return items


def union(parts):
    out = []
    for a, b in sorted(parts):
        if out and a <= out[-1][1]:
            out[-1] = (out[-1][0], max(b, out[-1][1]))
        else:
            out.append((a, b))
    return out


def phase(v, t):
    return v*t % 1


def dist(v, t):
    p = phase(v, t)
    return min(p, 1-p)


def clip_inequality(lo, hi, a, b):
    # a*t <= b
    if a > 0:
        hi = min(hi, b/a)
    elif a < 0:
        lo = max(lo, b/a)
    elif b < 0:
        return None
    return (lo, hi) if lo <= hi else None


def normalize_profile(pieces):
    # A profile is a union of labelled affine height pieces (lo,hi,slope,offset).
    out = []
    for p in sorted(set(pieces)):
        if out and out[-1][1] == p[0] and out[-1][2:] == p[2:]:
            out[-1] = (out[-1][0], p[1], p[2], p[3])
        else:
            out.append(p)
    return out


def envelope(lo, hi, lines, m):
    if not lines or lo > hi:
        return []
    if lo == hi:
        m.tick('line_evaluation', len(lines))
        return [(lo, hi, F(0), min(a*lo+b for a,b in lines))]
    events = {lo, hi}
    for (a,b),(c,d) in combinations(lines,2):
        m.tick('line_pair')
        if a != c:
            t = (d-b)/(a-c)
            if lo < t < hi:
                events.add(t)
    out = []
    points = sorted(events)
    for left,right in zip(points,points[1:]):
        mid = (left+right)/2
        m.tick('line_evaluation',len(lines))
        a,b = min(lines,key=lambda l:(l[0]*mid+l[1],l))
        out.append((left,right,a,b))
    return m.pieces(normalize_profile(out))


def threshold_profile(pieces, z, m):
    out = []
    for lo,hi,a,b in pieces:
        m.tick('threshold_clip')
        clipped = clip_inequality(lo,hi,-a,b-z)
        if clipped:
            out.append((*clipped,a,b))
    return m.pieces(normalize_profile(out))


def physical_profile(vs, m):
    events = sorted({F(k,2*v) for v in vs for k in range(2*v+1)})
    m.tick('tent_event',sum(2*v+1 for v in vs))
    out = []
    for lo,hi in zip(events,events[1:]):
        mid = (lo+hi)/2
        lines = []
        for v in vs:
            k = floor(v*mid)
            lines.append((F(v),F(-k)) if v*mid-k<F(1,2)
                         else (F(-v),F(k+1)))
        out.extend(envelope(lo,hi,lines,m))
    return m.pieces(normalize_profile(out))


def append_speed(pieces, v, z, m):
    out = []
    for lo,hi,a,b in pieces:
        if lo == hi:
            out.append((lo,hi,F(0),min(a*lo+b,dist(v,lo))))
            m.tick('added_point')
            continue
        events = sorted({lo,hi} | {F(k,2*v) for k in range(2*v+1)
                                  if lo<F(k,2*v)<hi})
        m.tick('added_event',2*v+1)
        for left,right in zip(events,events[1:]):
            mid=(left+right)/2
            k=floor(v*mid)
            line=(F(v),F(-k)) if v*mid-k<F(1,2) else (F(-v),F(k+1))
            out.extend(envelope(left,right,[(a,b),line],m))
    return threshold_profile(out,z,m)


def set_append(parts,v,z,m):
    out=[]
    for a,b in parts:
        for k in range(v):
            m.tick('set_band_pair')
            c,d=(k+z)/v,(k+1-z)/v
            if max(a,c)<=min(b,d):
                out.append((max(a,c),min(b,d)))
    return union(out)


def profile_optimum(pieces,m):
    if not pieces:
        return None,[]
    vals=[]
    for lo,hi,a,b in pieces:
        m.tick('profile_endpoint',2)
        vals.extend([(a*lo+b,lo),(a*hi+b,hi)])
    best=max(v for v,t in vals)
    for lo,hi,a,b in pieces:
        if lo<hi and a==0 and b==best:
            raise ValueError('maximizer plateau outside point-list grammar')
    return best,sorted({t for v,t in vals if v==best})


def hull_planes(vertices,m):
    planes=set()
    for u,v,w in combinations(vertices,3):
        m.tick('hull_triple')
        a=[v[i]-u[i] for i in range(3)]
        b=[w[i]-u[i] for i in range(3)]
        n=(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
        if n==(0,0,0):
            continue
        d=sum(n[i]*u[i] for i in range(3))
        signs=[sum(n[i]*p[i] for i in range(3))-d for p in vertices]
        m.tick('hull_side',len(vertices))
        if all(s<=0 for s in signs):
            pass
        elif all(s>=0 for s in signs):
            n=tuple(-x for x in n); d=-d
        else:
            continue
        scale=abs(next(x for x in n if x))
        planes.add(tuple(x/scale for x in n)+(d/scale,))
    return sorted(planes)


def parent_profile(cells,q,z,m):
    out=[]
    for planes in cells:
        for h in range(-1,q//2+1):
            m.tick('parent_slice')
            lo,hi=F(0),F(1,2)
            uppers=[]
            viable=True
            for a,b,c,d in planes:
                aa=a+b*q; dd=d+b*h
                m.tick('parent_inequality')
                if c>0:
                    uppers.append((-aa/c,dd/c))
                    bound=clip_inequality(lo,hi,aa,dd-c*z)
                elif c==0:
                    bound=clip_inequality(lo,hi,aa,dd)
                else:
                    # This fixed parent atlas has only the constant lower floor.
                    if aa != 0 or dd/c != z:
                        raise ValueError('unsupported nonconstant/lowered floor')
                    bound=(lo,hi)
                if bound is None:
                    viable=False; break
                lo,hi=bound
            if viable:
                out.extend(envelope(lo,hi,uppers,m))
    folded=normalize_profile(out)
    reflected=[(1-hi,1-lo,-a,a+b) for lo,hi,a,b in folded]
    return m.pieces(normalize_profile(folded+reflected))


def edge_profile(cells,q,z,m):
    out=[]
    for cell in cells:
        vertices=cell['vertices']
        for i,j in cell['edges']:
            p,r=vertices[i],vertices[j]
            delta=[r[k]-p[k] for k in range(3)]
            h0=q*p[0]-p[1]; dh=q*delta[0]-delta[1]
            for h in range(ceil(min(h0,h0+dh)),floor(max(h0,h0+dh))+1):
                m.tick('edge_integer_contact')
                if dh:
                    s=(h-h0)/dh
                    t=p[0]+s*delta[0]; height=p[2]+s*delta[2]
                    out.append((t,t,F(0),height))
                elif delta[0]:
                    a=delta[2]/delta[0]; b=p[2]-a*p[0]
                    out.append((min(p[0],r[0]),max(p[0],r[0]),a,b))
                else:
                    out.append((p[0],p[0],F(0),max(p[2],r[2])))
    out += [(1-hi,1-lo,-a,a+b) for lo,hi,a,b in list(out)]
    return threshold_profile(out,z,m)


def segment_profile(segments,q,z,m):
    out=[]
    for s in segments:
        lo,hi,c,d=map(F,(s['lo'],s['hi'],s['c'],s['d']))
        for h in range(ceil((q+d)*lo-c),floor((q+d)*hi-c)+1):
            m.tick('segment_integer_contact')
            t=(h+c)/(q+d)
            out.extend([(t,t,F(0),z),(1-t,1-t,F(0),z)])
    return m.pieces(normalize_profile(out))


def bounded_witness(segments,q,z,added,m):
    for s in segments:
        lo,hi,c,d=map(F,(s['lo'],s['hi'],s['c'],s['d']))
        h=ceil((q+d)*lo-c)
        m.tick('selector_round')
        if h<=(q+d)*hi-c:
            t=(h+c)/(q+d)
            m.tick('added_witness_check')
            if dist(added,t)>=z:
                return t
    return None


def decode_numbers(x):
    if isinstance(x,str):
        try:
            return F(x)
        except (ValueError,ZeroDivisionError):
            return x
    if isinstance(x,list):
        return [decode_numbers(a) for a in x]
    if isinstance(x,dict):
        return {k:decode_numbers(v) for k,v in x.items()}
    return x


def serialize(x):
    if isinstance(x,F):
        return str(x)
    if isinstance(x,dict):
        return {k:serialize(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [serialize(v) for v in x]
    return x


def witness_record(vs,t,m):
    if vs is None:
        return None
    m.tick('phase_lap',len(vs))
    return dict(time=t,laps=[floor(v*t) for v in vs],phases=[phase(v,t) for v in vs])


def answer(payload,query,mode,added,z,m):
    p=decode_numbers(payload); kind=p['kind']; q=p.get('q')
    m.tick('payload_dispatch')
    source_epoch=p['epoch']
    history=[]
    vs=None
    if 'rows' in p:
        vs=[int(a+b*q) for a,b in p['rows']]+[added]
    elif 'speeds' in p:
        vs=list(p['speeds'])+([added] if source_epoch=='parent' else [])
    complete=False; pieces=None; parts=None; best=None; times=None

    if kind=='scalar':
        if source_epoch=='parent':
            return dict(reason='parent scalar supplies no declared update rule',supported=False)
        if query=='Q1':
            m.tick('scalar_comparison')
            return dict(output=p['optimum']>=z,supported=True,reason='trusted scalar comparison')
        if query=='Q3':
            m.tick('cache_read')
            return dict(output=p['optimum'],supported=True,reason='trusted scalar read')
        return dict(supported=False,reason='no declared decoder for this scalar query')

    if kind=='optimizer_cache':
        best=p['optimum']; times=list(p['times'])
        if source_epoch=='parent':
            history.append('filter parent optimizers by added constraint')
            times=[t for t in times if dist(added,t)>=z]
            m.tick('cache_constraint_check',len(p['times']))
            best=None
        elif query in ('Q3','Q4'):
            m.tick('cache_read')
            return dict(output=best if query=='Q3' else times,supported=True,
                        reason='trusted child optimizer cache',history=history)
        parts=[(t,t) for t in times]
        complete=False

    elif kind=='threshold_set':
        parts=[tuple(pair) for pair in p['components']]
        if source_epoch=='parent':
            parts=set_append(parts,added,z,m)
            history.append('intersect retained complete parent set with new bands')
        complete=True

    elif kind=='profile':
        pieces=[tuple(piece) for piece in p['pieces']]
        if source_epoch=='parent':
            pieces=append_speed(pieces,added,z,m)
            history.append('cap retained parent envelope with new distance')
        else:
            pieces=threshold_profile(pieces,z,m)
        complete=True

    elif kind=='physical_generator':
        pieces=threshold_profile(physical_profile(vs,m),z,m)
        complete=True
        history.append('construct exact physical envelope from externally recovered speeds')

    elif kind=='segments':
        if mode=='internal':
            pieces=threshold_profile(physical_profile(vs,m),z,m)
            complete=True
            history.append('decode physical speeds from retained affine rows; reconstruct envelope')
        elif query in ('Q1','Q2'):
            t=bounded_witness(p['segments'],q,z,added,m)
            if t is None:
                return dict(supported=False,exhausted=True,reason='bounded selector found no contact')
            return dict(output=True if query=='Q1' else witness_record(vs,t,m),
                        supported=True,reason='pinned two-segment rounding and physical inverse')
        else:
            pieces=append_speed(segment_profile(p['segments'],q,z,m),added,z,m)
            history.append('enumerate only the two retained segment supports')

    elif kind=='edges':
        if mode=='internal':
            cells=[hull_planes(c['vertices'],m) for c in p['cells']]
            pieces=append_speed(parent_profile(cells,q,z,m),added,z,m)
            complete=True
            history.append('reconstruct convex parent facets from retained vertices, slice and cut')
        else:
            pieces=append_speed(edge_profile(p['cells'],q,z,m),added,z,m)
            history.append('intersect old edge support with integer orbit and new band')

    elif kind=='facets':
        pieces=append_speed(parent_profile(p['cells'],q,z,m),added,z,m)
        complete=True
        history.append('slice complete labelled parent inequalities and cut by new band')
    else:
        raise ValueError('unknown representation kind')

    if pieces is not None:
        parts=union([(a,b) for a,b,c,d in pieces])
        best,times=profile_optimum(pieces,m)
    if query=='Q1':
        return dict(output=bool(parts),supported=bool(parts) or complete,
                    exhausted=not parts and not complete,history=history,
                    reason='complete feasibility set' if complete else 'sound witness support')
    if query=='Q2':
        if not parts:
            return dict(supported=False,exhausted=True,history=history,reason='carrier has no safe time')
        record=witness_record(vs,parts[0][0],m)
        return dict(output=record,supported=record is not None,history=history,
                    reason='physical phase/lap inverse' if record else 'time available; phase/lap decoder absent')
    if query=='Q3':
        if best is None:
            return dict(supported=False,history=history,reason='objective height/update not retained')
        return dict(output=best,supported=complete,partial=not complete,history=history,
                    reason='complete height envelope' if complete else 'restricted-support maximum; no global upper certificate')
    if query=='Q4':
        if pieces is None:
            return dict(supported=False,history=history,reason='no child optimizing-set decoder')
        return dict(output=times,supported=complete,partial=not complete,history=history,
                    reason='complete height envelope' if complete else 'restricted-support maximizing times')
    if query=='Q5':
        return dict(output=parts,supported=complete,partial=not complete,history=history,
                    reason='complete closed union' if complete else 'only retained safe support')
    raise ValueError('unknown question')
