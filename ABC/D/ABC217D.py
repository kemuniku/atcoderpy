import bisect
import array
L,Q = map(int,input().split())
mokuzai = array.array('i', [0,L])
for _ in range(Q):
    c,x = map(int,input().split())
    if c == 1:
        mokuzai.insert(bisect.bisect(mokuzai,x), x)
    elif c == 2:
        i = bisect.bisect(mokuzai,x)
        print(mokuzai[i]-mokuzai[i-1])