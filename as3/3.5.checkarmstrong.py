def checkarmstrong(num):
    rec=num
    digit=[]
    while num!=0:
        digit.append(num%10)
        num//=10
    ans=0
    for el in digit:
        ans+=el**len(digit)
    if ans==rec:
        return True
    return False

y=int(input("Enter Number : "))
if checkarmstrong(y):
    print("Yes")
else :
    print("No")
        
