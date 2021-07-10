import math
N,M = map(int,input().split())
if(N>1):
    even = int(math.factorial(N)/(2*(math.factorial(N-2))))
else:
    even = 0
if(M>1):
    odd = int(math.factorial(M)/(2*(math.factorial(M-2))))
else:
    odd = 0
print(even + odd)
