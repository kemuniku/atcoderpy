from collections import deque
S = input()
Q = int(input())
d = deque(list(S))
reverse = False
for i in range(Q):
    Query = input().split()
    if Query[0] == "1":
        if reverse:
            reverse = False
        else:
            reverse = True
    elif(Query[1] == "1"):
        if reverse:
            d.append(Query[2])
        else:
            d.appendleft(Query[2])
    else:
        if reverse:
            d.appendleft(Query[2])
        else:
            d.append(Query[2])
ans = ""
if reverse:
    for _ in range(len(d)):
        ans += d.pop()
else:
    for _ in range(len(d)):
        ans += d.popleft()
print(ans)