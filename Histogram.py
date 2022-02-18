def histogram(list):
    for x in list:
        for i in range(int(x)):
            print("*",end='')
        print()
list = input().split()
histogram(list)