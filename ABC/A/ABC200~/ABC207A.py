a,b,c = map(int,input().split())
if(a +b >= c+b):
    if(a+b>a+c):
        print(a+b)
    else:
        print(a+c)
else:
    if(c+b>a+c):
        print(c+b)
    else:
        print(a+c)