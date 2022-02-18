class Movies:
    def __init__(self, name, imdb, category):
        self.name = name
        self.imdb = imdb
        self.category = category


m1 = Movies("Usual Suspects",7.0,"Thriller")
m2 = Movies("Hitman",6.3,"Action")
m3 = Movies("Dark Knight", 9.0, "Adventure")
m4 = Movies("The Help",8.0,"Drama")
m5 = Movies("The Choice",6.2,"Romance")
m6 = Movies("Colonia",7.4,"Romance")
m7 = Movies("Love",6.0,"Romance")
m8 = Movies("Bride Wars",5.4,"Romance")
m9 = Movies("Alphajet", 3.2, "War")
m10 = Movies("Ringing Crime", 4.0, "Crime")
m11 = Movies("Joking muck",7.2,"Comedy")
m12 = Movies("What is the name", 9.2, "Suspense")
m13 = Movies("Detective",7.0,"Suspense")
m14 = Movies("Exam",4.2,"Thriller")
m15 = Movies("We Two",7.2, "Romance")

print("Write the number of task: ")
a = int(input())

if a == 1:
    print("Which movie would you like to check?")
    name = input()
    if m1.name == name:
        if m1.imdb>5.5:
            print("True")
        else: print("False")
    elif m2.name == name:
        if m2.imdb>5.5:
            print("True")
        else: print("False")
    elif m3.name == name:
        if m3.imdb>5.5:
            print("True")
        else: print("False")
    elif m4.name == name:
        if m4.imdb>5.5:
            print("True")
        else: print("False")
    elif m5.name == name:
        if m5.imdb>5.5:
            print("True")
        else: print("False")
    elif m6.name == name:
        if m6.imdb>5.5:
            print("True")
        else: print("False")
    elif m7.name == name:
        if m7.imdb>5.5:
            print("True")
        else: print("False")
    elif m8.name == name:
        if m8.imdb>5.5:
            print("True")
        else: print("False")
    elif m9.name == name:
        if m9.imdb>5.5:
            print("True")
        else: print("False")
    elif m10.name == name:
        if m10.imdb>5.5:
            print("True")
        else: print("False")    
    elif m11.name == name:
        if m11.imdb>5.5:
            print("True")
        else: print("False")
    elif m12.name == name:
        if m12.imdb>5.5:
            print("True")
        else: print("False")
    elif m13.name == name:
        if m13.imdb>5.5:
            print("True")
        else: print("False")
    elif m14.name == name:
        if m14.imdb>5.5:
            print("True")
        else: print("False")
    elif m15.name == name:
        if m15.imdb>5.5:
            print("True")
        else: print("False")

if a == 2:
        if m1.imdb>5.5:
            print(m1.name)
        if m2.imdb>5.5:
            print(m2.name)
        if m3.imdb>5.5:
            print(m3.name)
        if m4.imdb>5.5:
            print(m4.name)
        if m5.imdb>5.5:
            print(m5.name)
        if m6.imdb>5.5:
            print(m6.name)
        if m7.imdb>5.5:
            print(m7.name)
        if m8.imdb>5.5:
            print(m8.name)
        if m9.imdb>5.5:
            print(m9.name)
        if m10.imdb>5.5:
            print(m10.name)
        if m11.imdb>5.5:
            print(m11.name)
        if m12.imdb>5.5:
            print(m12.name)
        if m13.imdb>5.5:
            print(m13.name)
        if m14.imdb>5.5:
            print(m14.name)
        if m15.imdb>5.5:
            print(m15.name)

if a == 3:
    cat = input()
    
    if m1.category == cat:
        print(m1.name)
    if m2.category == cat:
        print(m2.name)
    if m3.category == cat:
        print(m3.name)
    if m4.category == cat:
        print(m4.name)
    if m5.category == cat:
        print(m5.name)
    if m6.category == cat:
        print(m6.name)
    if m7.category == cat:
        print(m7.name)
    if m8.category == cat:
        print(m8.name)
    if m9.category == cat:
        print(m9.name)
    if m10.category == cat:
        print(m10.name)
    if m11.category == cat:
        print(m11.name)
    if m12.category == cat:
        print(m12.name)
    if m13.category == cat:
        print(m13.name)
    if m14.category == cat:
        print(m14.name)
    if m15.category == cat:
        print(m15.name)

if a == 4:
    print("Write down movie names in a line")
    names = input().split()
    avr = 0
    for x in names:
        if x == m1.name:
            avr +=m1.imdb
        if x == m2.name:
            avr +=m2.imdb        
        if x == m3.name:
            avr +=m3.imdb        
        if x == m4.name:
            avr +=m4.imdb        
        if x == m5.name:
            avr +=m5.imdb        
        if x == m6.name:
            avr +=m6.imdb        
        if x == m7.name:
            avr +=m7.imdb        
        if x == m8.name:
            avr +=m8.imdb        
        if x == m9.name:
            avr +=m9.imdb        
        if x == m10.name:
            avr +=m10.imdb        
        if x == m11.name:
            avr +=m11.imdb        
        if x == m12.name:
            avr +=m12.imdb        
        if x == m13.name:
            avr +=m13.imdb        
        if x == m14.name:
            avr +=m14.imdb        
        if x == m15.name:
            avr +=m15.imdb        
    avr = avr/len(names)
    print(avr)

if a==5:
    cat = input()
    avr = 0
    i = 0
    if m1.category == cat:
        avr +=m1.imdb
        i+=1
    if m2.category == cat:
        avr +=m2.imdb
        i+=1
    if m3.category == cat:
        avr +=m3.imdb
        i+=1
    if m4.category == cat:
        avr +=m4.imdb
        i+=1
    if m5.category == cat:
        avr +=m5.imdb
        i+=1
    if m6.category == cat:
        avr +=m6.imdb
        i+=1
    if m7.category == cat:
        avr +=m7.imdb
        i+=1
    if m8.category == cat:
        avr +=m8.imdb
        i+=1
    if m9.category == cat:
        avr +=m9.imdb
        i+=1
    if m10.category == cat:
        avr +=m10.imdb
        i+=1
    if m11.category == cat:
        avr +=m11.imdb
        i+=1
    if m12.category == cat:
        avr +=m12.imdb
        i+=1
    if m13.category == cat:
        avr +=m13.imdb
        i+=1
    if m14.category == cat:
        avr +=m14.imdb
        i+=1
    if m15.category == cat:
        avr +=m15.imdb
        i+=1

    avr = avr/i
    print(avr)
