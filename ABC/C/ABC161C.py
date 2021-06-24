N,K = map(int,input().split())
if(N%K >= K-(N%K)):
    print(K-(N%K))
else:
    print(N%K)