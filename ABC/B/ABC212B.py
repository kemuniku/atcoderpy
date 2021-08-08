X = list(input())
if(len(set(X)) == 1):
    print("Weak")
elif(str(int(X[0])+1)[-1] == X[1] and str(int(X[1])+1)[-1] == X[2] and str(int(X[2])+1)[-1] == X[3]):
    print("Weak")
else:
    print("Strong")