N = int(input())
A = list(map(int,input().split()))
ans = 0
while 1:
    for i in range(N):
        if A[i] % 2 == 1:
            break
        else:
            A[i] /= 2
    else:
        ans += 1
        continue
    break
    
print(ans)