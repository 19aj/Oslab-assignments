import math
while True:
    print("1. sum\n2. sin\n3. cos\n4. tan\n5. cot\n6. log\n7. Exit")
    sel=int(input("selection : "))
    if sel==1:
        n1=float(input("Num1 : "))
        n2=float(input("Num2 : "))
        print((n1),'+',(n2),'=',n1+n2)
    elif sel==2:
        n=float(input("Angle (degree) : "))
        print("sin(",n,') = ',math.sin(math.radians(n)))
    elif sel==3:
        n=float(input("Angle (degree) : "))
        print("cos(",n,') = ',math.cos(math.radians(n)))
    elif sel==4:
        n=float(input("Angle (degree) : "))
        print("tan(",n,') = ',math.tan(math.radians(n)))
    elif sel==5:
        n=float(input("Angle (degree) : "))
        print("cot(",n,') = ',1/math.tan(math.radians(n)))
    elif sel==6:
        n=-1
        while n<=0:
            n=float(input("Numerical value : "))
        print("log(",n,') = ',math.log(n))
        
    elif sel==7:
        break
