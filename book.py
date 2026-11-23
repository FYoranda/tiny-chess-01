import zlib,base64
T="AAAAZZZZFFKPCCFMAAAKC><ACFF7AAAA(-22-7AA2AFH2CHK2AHK2CFH-7AC(-227<<<<AAA<ACF<CCF<AFF<FFF<CAA7<<<AAAACFFF>AAA>AAA>AAA>AAA>AAA>AAAAAAC7<<><AAA<ACC>ACCAACC<CCC<ACA7<<>2--(2--(2--(2--(722-<777KKAAKPFA"
V={'P': 100, 'N': 320, 'B': 330, 'R': 500, 'Q': 900, 'K': 0}
A=[-33, -31, -18, -14, 14, 18, 31, 33]
D=[-17, -15, 15, 17]
R=[-16, -1, 1, 16]
B="c-n1~F>KpL7)H+mBhZQ(99%)Y3W9NQRpF`x={b@mI<^zpjwQ-<5+<=@IzkW{iXjRvVX2NFsjLu>8aZ+*Zse#@qehN5a^%R7-87a)kg1*ShQr<c-+SNEdD?5E6u(en)>ucZqa~edJ7L#&p0~u3z31lq_kP~*PYUWKk(@IuQrRzPrkdubOi)K*+ST3o<OEh=5pJmC#pz_gTCfe*Zq5OKCKtFt6YxsffPHu$cHkY@a}UI8@kjB?baipGNDd8sb=IVCei)G8D0sBk!q21z%7%5kLmTKtw~jwdC6-~bZ~P;%SCr^~@l3ZAWa*P>QrcI5g8U1ZblPg#d+rsyv3^(V+xzyl9kYzCNX=;`7|6N#8#iSY!HT<UCGaS$h@W^|+fX*~d9|Up^*!%+j+~D6VA4ba>+zykW3B3Xb-((%m-C1M#1xL<{v6JG)ugV>Gt6|e;U5#C(JCTqPJ$MK)!7p-NybwVmemAK4+RB+6a;YT8S*<gN>)j56Q-i1({>weq9%$@M!^O;0c&W0R$Mtsy5`3<NfWgLxd`3@fnAb&u&>2bql?Iu^njk(#QQQ_U9`mXWLN$PwiN-J;W8Ts9mfnWr{my2GyRHw+)Z>p&R)zepuxc7Z|~m~$GS-0`w6_MKENhxC~aj=izs@hBxRX?HauL!)GKL6>I7*%KpE$$gPb9b<C?RKKhH|cR2%eN#HkPnYR?CF$kOadnAEqsOTT_|Dd~*$m{sF&J^+H+*N}g0ug-Smb?`<8)fIOWH^Vq+;|d;eC_k2ge5vQ=XJ{R^<X!n({$3u~4Xv)dRr=n^d|>q^7wU5#Y=52Nmh<iX*S5e+mf)i>ax&uH#wG0nR!E<0l2eok8cJ^doFiudRwk|JNY#o%{RW7pPxNDNjhCIQQ{x$&^F+OZ1XL$+wJH4oUIr`tFq(A8cD<gLVUM~?ul~#L9EkKQ!@MU)h8(bsh+)jClL|U^6Zp^;f;<AKSlyzRdR@Ixe@0EZ%tk>R_qAoM$5nhaEO@WsZ3{$Zh86N<_M6%dI=(^c`gl4DjG#F)r@t_x+i_a*Rq#Q|I1yd#Rrf5~zw@8Yvf;~x*#&?9Ujt%RTdauZ)jiMX-icc9LO1m24^xqLv>F?QsVKn}x5wjl8|PJ-r|k`#SBzmMkU8O>IY0v|C6=sg_=)e(kJGYqiVA8;+r%bM=qOA|IR)PAkT^NC(@s8eDy55&zcK$aEKnh`AVUf?p?_UdQ1TMAOa*$6UPb<Xq|c}kB=y&z2>!guFzga<JT3c0AhBJU*l+Z_mYE{w;jqA3BJuZJ$zBcee2bRcqu{Z%g>&`?n&(Gh$u{&nYZ78_PxI_BB)%L--otL$-gfd{cD-z!;at?MqA0O_g=i->y5Clo{gcT^Z1L~He*qZM&PM"
def L():
 d=zlib.decompress(base64.b85decode(B));o=[];i=0
 while i<len(d):
  c=d[i];n=d[i+1];i+=2;m=[]
  for _ in range(n):
   v=d[i]*256+d[i+1];i+=2;f=v>>9;t=(v>>3)&63
   m.append(((f>>3)*16+(f&7),(t>>3)*16+(t&7),v&7))
  o.append((c,m))
 return o
LINES=L()
