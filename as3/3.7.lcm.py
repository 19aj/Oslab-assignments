def lcm(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    for i in range(n2,n1*n2+1,n2):
        if i%n1==0 and i%n2==0:
            return i


num1,num2=int(input("Enter Number1 : ")),int(input("Enter Number2 : "))

print("LCM : ",lcm(num1,num2))


