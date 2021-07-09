N = int(input())
sli = []
tli = []
for i in range(N):
    S,T = input().split()
    sli.append(S)
    tli.append(int(T))
tlisorted = sorted(tli)
print(sli[tli.index(tlisorted[-2])])