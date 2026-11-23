import json,os,urllib.request as q
E=os.environ["MAKEFUN_ENV_URL"]
def P_(p,b):
 with q.urlopen(q.Request(E+p,json.dumps(b).encode()))as s:return json.load(s)
V={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
T="AAAAZZZZFFKPCCFMAAAKC><ACFF7AAAA(-22-7AA2AFH2CHK2AHK2CFH-7AC(-227<<<<AAA<ACF<CCF<AFF<FFF<CAA7<<<AAAACFFF>AAA>AAA>AAA>AAA>AAA>AAAAAAC7<<><AAA<ACC>ACCAACC<CCC<ACA7<<>2--(2--(2--(2--(722-<777KKAAKPFA"
A=[-33,-31,-18,-14,14,18,31,33]
D=[-17,-15,15,17]
R=[-16,-1,1,16]
G=D+R
N=0
LIM=20000
def n(s):return not(s&136)
def a(b,s,w):
 d=1 if w else -1
 for o in(-15,-17):
  if n(s+d*o) and b[s+d*o]==('P' if w else 'p'):return 1
 for os,pc in((A,'N'),(G,'K')):
  for o in os:
   if n(s+o) and b[s+o]==(pc if w else pc.lower()):return 1
 for o in D+R:
  t=s+o
  while n(t):
   q=b[t]
   if q:
    if q in(('BQ' if o in D else 'RQ') if w else('bq' if o in D else 'rq')):return 1
    break
   t+=o
 return 0
class P:
 def __init__(s):
  s.b=list('RNBQKBNR')+['']*8+['P']*8+['']*72+['p']*8+['']*8+list('rnbqkbnr')+['']*8
  s.w=1;s.e=-1;s.k=(4,116)
def k(p,w):return p.k[not w]
def g(p):
 L=[];b=p.b;w=p.w
 def ap(s,t):
  if(t>>4)==(7 if w else 0):
   for r in 'QRBN':L.append((s,t,r if w else r.lower()))
  else:L.append((s,t,''))
 for s in range(128):
  if not n(s):continue
  c=b[s]
  if not c or c.isupper()!=w:continue
  u=c.upper()
  if u=='P':
   d=16 if w else -16
   o=s+d
   if n(o) and not b[o]:
    ap(s,o)
    t=s+2*d
    if(s>>4)==(1 if w else 6) and not b[t]:L.append((s,t,''))
   for o in(d-1,d+1):
    t=s+o
    if not n(t):continue
    q=b[t]
    if q and q.isupper()!=w:ap(s,t)
    elif t==p.e:L.append((s,t,''))
  elif u in 'NK':
   for o in(A if u=='N' else G):
    t=s+o
    if n(t) and(not b[t] or b[t].isupper()!=w):L.append((s,t,''))
  else:
   for o in(D if u=='B' else R if u=='R' else D+R):
    t=s+o
    while n(t) and not b[t]:L.append((s,t,''));t+=o
    if n(t) and b[t].isupper()!=w:L.append((s,t,''))
 O=[]
 for mv in L:
  q=m(p,mv)
  if not a(q.b,k(q,w),not w):O.append(mv)
 return O
def m(p,mv):
 f,t,pr=mv;q=P.__new__(P);q.b=p.b[:];q.w=p.w;q.e=p.e;q.k=p.k;b=q.b;c=b[f]
 b[t]=pr if pr else c;b[f]=''
 if c.upper()=='P' and t==p.e and not p.b[t]:b[t+(-16 if p.w else 16)]=''
 if c.upper()=='K':
  q.k=(t,q.k[1]) if p.w else(q.k[0],t)
  if abs(t-f)==2:
   rf=t+1 if t>f else t-2;rt=t-1 if t>f else t+1;b[rt]=b[rf];b[rf]=''
 q.e=(f+t)//2 if c.upper()=='P' and abs(t-f)==32 else -1
 q.w=not p.w
 return q
def e(p):
 s=0;wb=0;bb=0
 for i in range(128):
  if not n(i):continue
  c=p.b[i]
  if not c:continue
  u=c.upper();d=1 if c.isupper() else -1;f=i&7
  if f>3:f=7-f
  r=7-(i>>4) if d>0 else i>>4
  s+=(V[u]+2*(ord(T['PNBRQK'.index(u)*32+r*4+f])-65))*d
  if u=='B':wb+=d>0;bb+=d<0
 if wb>1:s+=30
 if bb>1:s-=30
 return s if p.w else -s
def o(L,p):
 L.sort(key=lambda mv:V.get(p.b[mv[1]].upper(),0)*10+(1000 if mv[2] else 0),reverse=True)
 return L
def s(p,d,al,be):
 global N;N+=1
 if N>LIM:return e(p)
 if d<=0:
  st=e(p)
  if st>=be:return be
  if st>al:al=st
  L=[mv for mv in g(p) if p.b[mv[1]] or mv[1]==p.e]
 else:
  L=g(p)
  if not L:return -100000-d if a(p.b,k(p,p.w),not p.w) else 0
 for mv in o(L,p):
  v=-s(m(p,mv),d-1,-be,-al)
  if v>=be:return be
  if v>al:al=v
 return al
def b(p,L):
 global N
 bm=L[0];N=0
 for d in(1,2,3,4,5,6):
  al=-10**9;bv=-10**9;cm=bm
  for mv in o(L,p):
   v=-s(m(p,mv),d-1,-10**9,-al)
   if v>bv:bv=v;cm=mv
   if v>al:al=v
   if N>LIM:break
  if N>LIM:break
  bm=cm
 return bm
def h(s):return chr(97+(s&7))+str((s>>4)+1)
def u(mv):return h(mv[0])+h(mv[1])+(mv[2].lower() if mv[2] else '')
def w(x):return(ord(x[0])-97)+(int(x[1])-1)*16
def c(x,p):return(w(x[:2]),w(x[2:4]),(x[4].upper() if p.w else x[4].lower()) if len(x)>4 else '')
def main():
 while 1:
  g=P_("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   p=P()
   for y in g["moves"]:p=m(p,c(y,p))
   L=[c(x,p) for x in g["legal_moves"]]
   g=P_("/move",{"game":g["game"],"move":u(b(p,L))})
if __name__=="__main__":main()
