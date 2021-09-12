H,W = map(int,input().split())
A = []
width_sums = []
height_sums = []
for i in range(H):
    li = list(map(int,input().split()))
    A.append(li)
    width_sums.append(sum(li))
for i in range(W):
    height_sum = 0
    for j in range(H):
        height_sum += A[j][i]
    height_sums.append(height_sum)
for i in range(H):
    li =[]
    for j in range(W):
        li.append(width_sums[i]+height_sums[j]-A[i][j])
    print(*li)