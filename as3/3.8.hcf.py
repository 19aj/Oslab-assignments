def hcf(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    for i in range(n1,0,-1):
        if n1%i==0 and n2%i==0:
            return i


num1,num2=int(input("Enter Number1 : ")),int(input("Enter Number2 : "))


print("HCF : ",hcf(num1,num2))


