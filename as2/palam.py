from random import randint
u=0
c1=0
c2=0
for i in range(0,5):
    user=0
    while(user<1 or user>2):
        print("1.Roo\n2.posht")
        user=int(input("selection : "))
    com1=randint(1,2)
    com2=randint(1,2)
    if user==com1 and com1==com2 and user==com2:
        u+=1
        c1+=1
        c2+=1
        print("equal")
    elif user!=com1 and user!=com2:
        u+=1
        print("user wins")
    elif user!=com1 and com1!=com2:
        c1+=1
        print("computer1 wins")
    elif com2!=com1 and user!=com2:
        c2+=1
        print("computer2 wins")
print("-----------------------------------------")
print("user : ",u)
print("computer1 : ",c1)
print("computer2 : ",c2)
        