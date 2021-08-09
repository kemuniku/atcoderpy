N,X = map(int,input().split())
sum_alc = 0
for i in range(N):
    v,p = map(int,input().split())
    sum_alc += v*p
    if(sum_alc > X*100):
        print(i+1)
        break
else:
    print(-1)