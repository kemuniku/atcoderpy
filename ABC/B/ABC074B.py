N = int(input())
K = int(input())
li = list(map(int,input().split()))
ans = 0
for i in li:
    if(i > abs(i-K)):
        ans += 2*abs(i-K)
    else:
        ans += 2*i
print(ans)