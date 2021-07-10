li = list(map(int,input().split()))
ans = 0
for i in range(2):
    if(li[0]>=li[1]):
        ans += li[0]
        li[0] = ans-1
    else:
        ans += li[1]
        li[1] = ans-1
print(ans)