def spy_game(list):
    z1=0
    z2=0
    s=0
    
    for i in range(len(list)):
        if int(list[i])==0 and z1==0:
            z1 = 1
        if int(list[i])==0 and z1==1:
            z2 = 1
        if int(list[i])==7 and z2==1:
            s=1

    if z1+z2+s==3:
        print("True")
    else: 
        print ("False")

list = input().split()
spy_game(list)