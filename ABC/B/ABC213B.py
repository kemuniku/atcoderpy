N = input()
A = list(map(int,input().split()))
a_sorted = sorted(A)
print(A.index(a_sorted[-2])+1)