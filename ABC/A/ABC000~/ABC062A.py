x,y = map(int,input().split())
g1 = [1,3,5,7,8,10,12]
g2 =  [4,6,9,11]
if x in g1:
    if y in g1:
        print("Yes")
    else:
        print("No")
elif x in g2:
    if y in g2:
        print("Yes")
    else:
        print("No")
else:
    if y == 2:
        print("Yes")
    else:
        print("No")