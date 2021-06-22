li = list(map(int,input().split()))
li.sort()
if(li[2]-li[1]==li[1]-li[0]):
    print("Yes")
else:
    print("No")