N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
i = T.index(min(T))
for _ in range(N):
    sunuke_from = T[i]
    if i == N-1:
        sunuke_to_index = 0
    else:
        sunuke_to_index = i+1
    sunuke_to = T[sunuke_to_index]
    if(sunuke_to > sunuke_from+S[i]):
        T[sunuke_to_index] = sunuke_from+S[i]
    i = sunuke_to_index
for j in T:
    print(j)