N = int(input())
ans = 0
for i in range(N):
    ans = ans + (i+1)*10000/N
print(ans)