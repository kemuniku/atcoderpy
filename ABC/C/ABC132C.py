N = int(input())
li = list(map(int,input().split()))
li.sort()
print(li[int(N/2)]-li[int(N/2-1)])