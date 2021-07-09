S = list(input())
li = list(set(S))
if len(li) == 4:
    print("Good")
else:
    b = False
    for i in range(3):
        if S[i] == S[i+1]:
            b = True
    if b:
        print("Bad")
    else:
        print("Good")