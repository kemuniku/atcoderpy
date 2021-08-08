S = input()
i = 0
li = [0]
for s in S:
    if s in "ACGT":
        i = i + 1
    else:
        li.append(i)
        i=0
li.append(i)
print(max(li))