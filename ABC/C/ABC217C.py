N = int(input())
q = list(map(int,input().split()))
list = list(range(N))
for i in range(N):
    list[q[i]-1] = i+1
print(*list)