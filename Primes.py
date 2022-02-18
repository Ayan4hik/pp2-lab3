def filter_prime(a):
    str = "Prime"
    for i in range(2,a):
        if(a%i==0):
            str="No"
    if(str=="Prime"):
        print(a, end=" ")

list = input().split()
for i in range(len(list)):
    filter_prime(int(list[i]))