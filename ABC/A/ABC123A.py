a =int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
li = [a,b,c,d,e]
ans = "Yay!"
for i in range(5):
    for h in range(i,5):
        if(li[h]-li[i] > k):
            ans = ":("
print(ans)