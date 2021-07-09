li = list(input())
ans = "Yes"
for S in set(li):
    if(li.count(S)%2 != 0):
        ans = "No"
print(ans)