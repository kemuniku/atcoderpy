sheet = [list(map(int,input().split())),list(map(int,input().split())),list(map(int,input().split()))]
after = [[False for i in range(3)] for j in range(3)]
n = int(input())
for z in range(n):
    num = int(input())
    for i in range(3):
        li = sheet[i]
        for j in range(3):
            if li[j] == num:
                after[i][j] = True
print("Yes" if after[0][0] and after[1][0] and after[2][0] or after[0][1] and after[1][1] and after[2][1] or after[0][2] and after[1][2] and after[2][2] or after[0][0] and after[0][1] and after[0][2] or after[1][0] and after[1][1] and after[1][2] or after[2][0] and after[2][1] and after[2][2] or after[0][0] and after[1][1] and after[2][2] or after[0][2] and after[1][1] and after[2][0] else "No")