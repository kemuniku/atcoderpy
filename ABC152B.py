a,b = map(int,input().split())
sa,sb = "",""
for i in range(b):
    sa = sa + str(a)
for i in range(a):
    sb = sb + str(b)
if(sa>=sb):
    print(sb)
else:
    print(sa)