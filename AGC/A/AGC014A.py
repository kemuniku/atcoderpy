A,B,C = map(int,input().split())
i = 0
if(A==B==C and A%2 == 0 and B%2 == 0 and C%2 == 0):
    print(-1)
    exit()
while A%2 == 0 and B%2 == 0 and C%2 == 0:
    ha,hb,hc =A/2 , B/2 , C/2
    A = hb+hc
    B = ha+hc
    C = ha+hb
    i += 1
print(i)