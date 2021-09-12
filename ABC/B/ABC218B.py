Alphabet = "abcdefghijklmnopqrstuvwxyz"
P = list(map(int,input().split()))
ans = ""
for i in P:
    ans += Alphabet[i-1]
print(ans)