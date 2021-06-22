S = input()
output = ""
for s in S[::-1]:
    if(s=="6"):
        output += "9"
    elif(s=="9"):
        output += "6"
    else:
        output += s
print(output)