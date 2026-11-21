import sys
V={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
A=[-33,-31,-18,-14,14,18,31,33]
D=[-17,-15,15,17]
R=[-16,-1,1,16]
G=D+R
def n(s): return not(s&136)
def a(b,s,w):
 d=1 if w else -1
 for o in(-15,-17):
  if n(s+d*o) and b[s+d*o]==('P' if w else 'p'): return 1
 for os,pc in((A,'N'),(G,'K')):
  for o in os:
   if n(s+o) and b[s+o]==(pc if w else pc.lower()): return 1
 for o in D+R:
  t=s+o
  while n(t):
   q=b[t]
   if q:
    if q in(('BQ' if o in D else 'RQ') if w else('bq' if o in D else 'rq')): return 1
    break
   t+=o
 return 0
class P:
 def __init__(s):
  s.b=['']*128
  for f in range(8):
   s.b[f]='RNBQKBNR'[f]; s.b[112+f]='rnbqkbnr'[f]; s.b[16+f]='P'; s.b[96+f]='p'
  s.w=1; s.c='KQkq'; s.e=-1
def k(p,w): return next(i for i in range(128) if p.b[i]==('K' if w else 'k'))
def g(p):
 L=[]; b=p.b; w=p.w
 def ap(s,t):
  if(t>>4)==(7 if w else 0):
   for r in 'QRBN': L.append((s,t,r if w else r.lower()))
  else: L.append((s,t,''))
 for s in range(128):
  if not n(s): continue
  c=b[s]
  if not c or c.isupper()!=w: continue
  u=c.upper()
  if u=='P':
   d=16 if w else -16
   o=s+d
   if n(o) and not b[o]:
    ap(s,o)
    t=s+2*d
    if(s>>4)==(1 if w else 6) and not b[t]: L.append((s,t,''))
   for o in(d-1,d+1):
    t=s+o
    if not n(t): continue
    q=b[t]
    if q and q.isupper()!=w: ap(s,t)
    elif t==p.e: L.append((s,t,''))
  elif u in 'NK':
   for o in(A if u=='N' else G):
    t=s+o
    if n(t) and(not b[t] or b[t].isupper()!=w): L.append((s,t,''))
  else:
   for o in(D if u=='B' else R if u=='R' else D+R):
    t=s+o
    while n(t) and not b[t]: L.append((s,t,'')); t+=o
    if n(t) and b[t].isupper()!=w: L.append((s,t,''))
 for w2 in(w,):
  o=0 if w2 else 112
  for kt,rf,em,at in((6,7,(5,6),(4,5,6)),(2,0,(3,2,1),(4,3,2))):
   r='KQ'[kt==2] if w2 else 'kq'[kt==2]
   if r in p.c and all(not b[o+x] for x in em) and b[o+4]==('K' if w2 else 'k') and b[o+rf]==('R' if w2 else 'r') and all(not a(b,o+x,not w2) for x in at): L.append((o+4,o+kt,''))
 O=[]
 for mv in L:
  q=m(p,mv)
  if not a(q.b,k(q,w),not w): O.append(mv)
 return O
def m(p,mv):
 f,t,pr=mv; q=P.__new__(P); q.b=p.b[:]; q.w=p.w; q.c=p.c; q.e=p.e; b=q.b; c=b[f]
 b[t]=pr if pr else c; b[f]=''
 if c.upper()=='P' and t==p.e and not p.b[t]: b[t+(-16 if p.w else 16)]=''
 if c.upper()=='K' and abs(t-f)==2:
  rf=t+1 if t>f else t-2; rt=t-1 if t>f else t+1; b[rt]=b[rf]; b[rf]=''
 R={4:'KQ',116:'kq',7:'K',0:'Q',119:'k',112:'q'}
 for sq in(f,t):
  if sq in R:
   for ch in R[sq]: q.c=q.c.replace(ch,'')
 q.e=(f+t)//2 if c.upper()=='P' and abs(t-f)==32 else -1
 q.w=not p.w
 return q
def e(p):
 s=0
 for i in range(128):
  if not n(i): continue
  c=p.b[i]
  if not c: continue
  s+=V[c.upper()]*(1 if c.isupper() else -1)
 return s if p.w else -s
def o(L,p):
 L.sort(key=lambda mv:(V[p.b[mv[1]].upper()] if p.b[mv[1]] else 0)*10-(V[p.b[mv[0]].upper()]//50)+(1000 if mv[2] else 0),reverse=True)
 return L
def s(p,d,al,be):
 if d<=0:
  st=e(p)
  if st>=be: return be
  if st>al: al=st
  L=[mv for mv in g(p) if p.b[mv[1]] or mv[1]==p.e]
 else:
  L=g(p)
  if not L: return -100000 if a(p.b,k(p,p.w),not p.w) else 0
 for mv in o(L,p):
  v=-s(m(p,mv),d-1,-be,-al)
  if v>=be: return be
  if v>al: al=v
 return al
def b(p,d):
 L=o(g(p),p)
 bm=L[0]; bv=al=-10**9
 for mv in L:
  v=-s(m(p,mv),d-1,-10**9,-al)
  if v>bv: bv=v; bm=mv
  if v>al: al=v
 return bm
def h(s): return chr(97+(s&7))+str((s>>4)+1)
def u(mv): return h(mv[0])+h(mv[1])+(mv[2].lower() if mv[2] else '')
def w(x): return(ord(x[0])-97)+(int(x[1])-1)*16
def c(x,p): return(w(x[:2]),w(x[2:4]),(x[4].upper() if p.w else x[4].lower()) if len(x)>4 else '')
def main():
 p=P()
 for l in sys.stdin:
  t=l.split()
  if not t: continue
  x=t[0]
  if x in('uci','isready'): print('id name t\nuciok' if x=='uci' else 'readyok',flush=True)
  elif x=='position' and t[1]=='startpos':
   p=P()
   if len(t)>2 and t[2]=='moves':
    for y in t[3:]: p=m(p,c(y,p))
  elif x=='go': print('bestmove',u(b(p,3)),flush=True)
if __name__=='__main__': main()
