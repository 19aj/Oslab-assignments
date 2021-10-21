def checkfactorial(num) :
    f=1
    a=1
    while a<=num:
        f=a*f
        a+=1
        if f==num:
            return True
    return False

x=int(input("Enter Number : "))
if checkfactorial(x):
    print('Yes')
else :
    print('No')
