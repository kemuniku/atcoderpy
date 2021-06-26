a,b,c,d = map(int,input().split())
if(c*d<=b and a+b > c*d):
    print(-1)
else:
    blue=a
    red=0
    i=0
    while(blue>red*d):
        blue += b
        red += c
        i += 1
    print(i)