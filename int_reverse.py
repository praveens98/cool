num=int(input('enter the number: '))
res=0
while num>0:
  rem=num%10  #to get the last digit 
  res=res*10+rem
  num//=10
 print(res)
