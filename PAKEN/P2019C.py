n,m=map(int,input().split())
scores = [list(map(int,input().split())) for i in range(n)]
sum_scores = []
for i in range(m):
    for j in range(i,m):
        sum_score = 0
        for li in scores:
            sum_score += max([li[i],li[j]])
        sum_scores.append(sum_score)
print(max(sum_scores))
