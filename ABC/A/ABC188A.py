li = list(map(int,input().split()))
li.sort()
if(li[0]+3>li[1]):
    print("Yes")
else:
    print("No")