K,N = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
distances = []
if(abs(li[0] - li[N-1]+K) >= li[1] - li[0]):
    distances.append(K-abs(li[0] - li[N-1]+K))
else:
    distances.append(K-li[1] + li[0])
for i in range(1,N-1):
    if(li[i] - li[i-1] >= li[i+1] - li[i]):
        distances.append(K-li[i] + li[i-1])
    else:
        distances.append(K-li[i+1] + li[i])
if(li[N-1] - li[N-2] >= abs(li[0] - li[N-1]+K)):
    distances.append(K-li[N-1] + li[N-2])
else:
    distances.append(K-abs(li[0] - li[N-1])+K)
print(min(distances))