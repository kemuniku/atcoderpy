import decimal
N,K = map(int,input().split())
noli = list(map(int,input().split()))
sortnoli = sorted(noli)
if(K%N == 0):
    for i in noli:
        print(int(K//N))
else:
    A = sortnoli[K%N-1]
    for i in noli:
        if(i<=A):
            print(K//N+1)
        else:
            print(K//N)