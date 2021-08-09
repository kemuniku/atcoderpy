N = input()
ans = False
for i in range(10):
    s = "0"*i + N
    if(s == s[::-1]):
        ans = True
if ans:
    print("Yes")
else:
    print("No")