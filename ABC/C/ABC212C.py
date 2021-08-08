N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.sort()
ans = []
for a in A:
    if(len(B) == 1):
        ans.append(abs(B[0]-a))
    elif(len(B) == 2):
        ans.append(min([abs(B[0]-a),abs(B[1]-a)]))
    else:
        head = 0
        tail = len(B) - 1
        near_number = None
        min_diff = float('inf')
        while head <= tail:
            center = tail + (head - tail) // 2
            min_diff_right = float('inf')
            min_diff_left =float('inf')
            if center + 1 < len(B):
                min_diff_right = abs(B[center+1] - a)
            if center > 0:
                min_diff_left = abs(B[center-1] - a)
            
            if min_diff_left < min_diff:
                min_diff = min_diff_left
                near_number = B[center-1]
            if min_diff_right < min_diff:
                min_diff = min_diff_right
                near_number = B[center+1]
                
            if B[center] == a:
                ans.append(0)
                break
            elif B[center] < a:
                head = center + 1
            else:
                tail = center - 1
        else:
            ans.append(abs(min_diff))
print(min(ans))
