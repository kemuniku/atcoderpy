N = int(input())
li=[list(map(int,input().split())) for i in range(N)]
ans = 0
for i in range(N-1):
    aline = li[i][0]
    astart = li[i][1]
    aend = li[i][2]
    for j in range(i+1,N):
        bline = li[j][0]
        bstart = li[j][1]
        bend = li[j][2]
        if(bstart == aend):
            if((aline == 1 or aline == 3) and (bline == 1 or bline == 2)):
                ans += 1
        elif(bend == astart):
            if((aline == 1 or aline == 2) and (bline == 1 or bline == 3)):
                ans += 1
        elif(bstart <= aend and astart <= bend):
            ans += 1
print(ans)