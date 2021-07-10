import math
MOD = 1000000007
N = int(input())
C = list(map(int,input().split()))
C.sort()
k = 1
for i in range(N):
    k = k * (C[i]-i) % MOD
print(k)
