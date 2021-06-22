n = int(input())
s,t = map(str,input().split())
answer = ""
for i in range(n):
    answer = answer + s[i] + t[i]
print(answer)