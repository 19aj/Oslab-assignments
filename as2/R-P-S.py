from random import randint
u=0
c=0
for i in range(0,5):
    user=4
    while(user<1 or user>3):
        print("1. Rock\n2. Paper\n3.Scissors")
        user=int(input("selection : "))
    com=randint(1,3)
    if (user==com):
        u+=1
        c+=1
    elif(user==1 and com==2):
        c+=1
        print("computer wins")
    elif(user==2 and com==1):
        u+=1
        print("User wins")
    elif(user==1 and com==3):
        u+=1
        print("User wins")
    elif(user==3 and com==1):
        c+=1
        print("computer wins")
    elif(user==2 and com==3):
        c+=1
        print("computer wins")
    elif(user==3 and com==2):
        u+=1
        print("User wins")
    
if u>c:
    print("User is winner")
else:
    print("Computer is winner")
    
    