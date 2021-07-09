import math
P = int(input())
count = 0
for i in range(10):
    j = math.factorial(10-i)
    count = count +(P-P%j)/j
    P = P%j
print(int(count))