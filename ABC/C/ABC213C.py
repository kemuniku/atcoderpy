import bisect
H,W,N = map(int,input().split())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
sorted_A = list(sorted(set(A)))
sorted_B = list(sorted(set(B)))
for i in range(N):
    print(bisect.bisect_right(sorted_A,A[i]),bisect.bisect_right(sorted_B,B[i]))