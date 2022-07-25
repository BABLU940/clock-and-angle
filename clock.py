#clock and angle
t=int(input())
while(t>0):
  h,m=map(int,input().split())
  h=h*(360//12)+(m*360)//(12*60)
  m=m*(360//60)
  ang=abs(h-m)
  if(360-ang):
      print(ang)
  else:
    ang=(180-ang)
    print(ang)
  t=t-1