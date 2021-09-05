H,W = map(int,input().split())
li = []
for i in range(H):
    s = input()
    if s != "."*W:
        li.append(s)
for i in range(W):
    count = 0
    for j in range(len(li)):
        if li[j][i] == ".":
            count += 1
    if count == len(li):
        for j in range(len(li)):
            li[j] = li[j][:i] + "z"+li[j][i+1:]
for s in li:
    print(s.replace("z",""))