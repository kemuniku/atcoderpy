S = list(input())
li = list(set(S))
if len(li) == 2:
    if(S.count(li[0])==2):
        print("Yes")
    else:
        print("No")
else:
    print("No")