N = int(input())
xy = []
X = {}
Y = {}
ans = 0
for i in range(N):
    li = list(map(int,input().split()))
    if li[0] in X.keys():
        X[li[0]].append(li[1])
    else:
        X[li[0]] = [li[1]]
    if li[1] in Y.keys():
        Y[li[1]].append(li[0])
    else:
        Y[li[1]] = [li[0]]
for i in X.keys():
    Ys = X[i]
    #YsはX座標が同じな点のY座標
    if(len(Ys) != 1):
        Xs = []
        for y in Ys:
            if(y in Y.keys()):
                Xs.append([k for k in Y[y] if k>i])
        for xlist in Xs:
            for x in xlist:
                ans += len(set(Ys) & set(X[x])) -1
print(ans//2)
