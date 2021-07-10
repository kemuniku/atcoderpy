N,X = map(int,input().split())
li = list(map(int,input().split()))
for i in range(N):
    if((i+1)%2 == 0):
        li[i] = li[i] - 1
if(X>=sum(li)):
    print("Yes")
else:
    print("No")