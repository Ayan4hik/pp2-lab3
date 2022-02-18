def has_33(list):
    a = "False"
    for i in range(len(list)-1):
        if int(list[i])==3 and int(list[i+1])==3:
            a = "True"
    print(a)

list = input().split()
has_33(list)