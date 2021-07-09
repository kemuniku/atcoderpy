N = int(input())
if(N%1000 == 0):
    print(0)
else:
    print(1000-int(N%1000))