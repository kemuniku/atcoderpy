A,B,X = map(int,input().split())
if(X<A):
    print("NO")
elif(B >= X-A):
    print("YES")
else:
    print("NO")