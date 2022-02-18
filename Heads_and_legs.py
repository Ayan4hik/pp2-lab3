def solve(h,l):
    for r in range(h):
        if r*4+(h-r)*2==l:
            print("Rabbits: "+ str(r))
            print("Chickens: " + str(h-r))
print("How many heads do we have?")    
heads = int(input())
print("How many legs do we have?")
legs= int(input())
solve(heads,legs)