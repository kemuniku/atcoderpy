N,S,D = map(int,input().split())
ans = "No"
for i in range(N):
    x,y = map(int,input().split())
    if x<S and y>D:
        ans = "Yes"
print(ans)