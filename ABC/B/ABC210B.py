N = int(input())
S = input()
ans = "Takahashi"
for i in S:
    if(i == "1"):
        print(ans)
        break
    else:
        if(ans == "Takahashi"):
            ans = "Aoki"
        else:
            ans = "Takahashi"