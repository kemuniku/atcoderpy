y,m,d= map(int,input().split("/"))
if(y<=2019):
    if(m<=4):
        if(d<=30):
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")
else:
    print("TBD")