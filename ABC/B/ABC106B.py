N = int(input())
count = 0
i = 1
while i <= N:
    j = 1
    y = 0
    while j <=i:
        if(i%j == 0):
            y += 1
        j += 1
    if(y == 8):
        count += 1
    i += 2
print(count)