import math
def volume(r):
    V = (int(r)**3)*math.pi*4/3 #formula V=4/3*pi*r^3
    return V

r = int(input())
print (volume(r))