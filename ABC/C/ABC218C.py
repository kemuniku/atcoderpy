def comp(li):
    while li[0] == ["."]*N:
        li.pop(0)
    while li[-1] == ["."]*N:
        li.pop(-1)
    while 1:
        for i in range(len(li)):
            if li[i][0] != ".":
                break
        else:
            for i in range(len(li)):
                li[i].pop(0)
            continue
        break
    while 1:
        for i in range(len(li)):
            if li[i][-1] != ".":
                break
        else:
            for i in range(len(li)):
                li[i].pop(-1)
            continue
        break
    return li


N = int(input())
S = []
T = []
for _ in range(N):
    S.append(list(input()))
for _ in range(N):
    T.append(list(input()))

S = comp(S)
T = comp(T)

#参考記事:https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c
#参考記事:https://hibiki-press.tech/python/zip-iterable/3834
if(S==T):
    print("Yes")
elif(S == list(map(list,zip(*T[::-1])))):
    print("Yes")
elif(S == list(map(list,list(zip(*T))[::-1]))):
    print("Yes")
else:
    li = []
    for t in T:
        li.append(t[::-1])
    if S == li[::-1]:
        print("Yes")
    else:
        print("No")
