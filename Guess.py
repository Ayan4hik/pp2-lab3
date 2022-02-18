import random
num = random.randint(1,20)

def guess(n):
    x = int(input())
    if x<num:
        print("Your guess is too low.")
        print("Take a guess.")
        guess(n+1)
    elif x>num:
        print("Your guess is too high.")
        print("Take a guess.")
        guess(n+1)
    elif x==num:
        print ("Good job, "+ name + "!",end=' ')
        print("You guessed my number in " + str(n) + " guesses!")

print("Hello! What is your name?")
name = input()
print("Well, "+name+", I am thinking of a number between 1 and 20.")
print("Take a guess.")
  
guess(1)

#Actually, I made a game like this in C++.  The computer must to guess your number.


#include <bits/stdc++.h>
# using namespace std;
# int main(){
#     cout << "Zagadaite chislo ot 1 do 1000"<<endl;
#     int l = 0;
#     int r = 1001;
#     int m = (l+r)/2;
#     int a=0;
#     while(a!=3){
#         cout << "Vvedit 1 esli vashe chislo bolshe chem " << m<<endl;
#         cout << "Vvedit 2 esli vashe chislo menshe chem " << m<<endl;
#         cout << "Vvedit 3 esli vashe chislo rovno " << m<<endl;
#         cin >> a;
#         if(a == 1){
#             l = m;
#             m = (l+r)/2;
#         }
#         if(a == 2){
#             r = m;
#             m = (l+r)/2;
#         }
#         if(a == 3){
#             cout << "vashe chislo: "<< m<<endl;
#         }
#     }
# }


#To uncomment the code above, click ctrl+/