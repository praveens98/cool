num=5591614
res=0
while num>0:
  rem=num%10
  res=res*10+rem
  num//=10
 print(res)
