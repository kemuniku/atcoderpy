N,S,T = map(int,input().split())
W = int(input())
if(S<=W and W<=T):
    count = 1
else:
    count = 0
for i in range(N-1):
    A = int(input())
    W = W + A
    if(S<=W and W<=T):
        count += 1
print(count)