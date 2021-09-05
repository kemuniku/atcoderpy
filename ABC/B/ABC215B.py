N = int(input())
i = 0
while N >= 2**i:
    i += 1
print(i-1)