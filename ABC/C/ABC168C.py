import math
a,b,h,m = map(int,input().split())
h=30*h+0.5*m
if(abs(h-6*m) <=180):
    cos = math.cos(math.radians(abs(h-6*m)))
else:
    cos = math.cos(math.radians(360-abs(h-6*m)))
print(math.sqrt(a**2 + b**2 - 2*a*b*cos))