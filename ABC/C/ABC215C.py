import math
S,K = input().split()
K = int(K)
set_S = sorted(list(set(S)))
count_S =[]
for s in set_S:
    count_S.append(S.count(s))

fact_S = list(map(math.factorial,count_S))
kumiawase =1
for i in fact_S:
    kumiawase *= i
ans = ""
for i in range(len(S)):
    k = 0
    for j in range(len(S)):
        before = k
        k += math.factorial(len(S)-i-1)/kumiawase * count_S[j]
        if(K<=int(k)): 
            ans += set_S[j]
            count_S[j] -= 1
            if(count_S[j] == 0):
                set_S.pop(j)
                count_S.pop(j)
            fact_S = list(map(math.factorial,count_S))
            kumiawase =1
            for i in fact_S:
                kumiawase *= i
            K -= before
            break
print(ans)