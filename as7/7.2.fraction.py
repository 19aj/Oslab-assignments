class fraction:
    def __init__(self,numerator,denominator):
        self.n=numerator
        self.d=denominator
    def __add__(self,of):
        if self.d==of.d:
            return fraction(self.n+of.n , of.d)
        else :
            return fraction(self.n*of.d + self.d*of.n , self.d*of.d)
    def __sub__(self,of):
        if self.d==of.d:
            return fraction(self.n-of.n , of.d)
        else :
            return fraction(self.n*of.d - self.d*of.n , self.d*of.d)
    def __mul__(self,of):
            return fraction(self.n*of.n , self.d*of.d)
    def __truediv__(self,of):
            return fraction(self.n*of.d , self.d*of.n)
    def __str__(self):
        return str(self.n)+'/'+str(self.d)
    
while True:
    print('1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Exit')
    choice=int(input('Chioce : '))
    fn,fd=input('First Fraction : ').split('/')
    f1=fraction(int(fn),int(fd))
    fn,fd=input('Second Fraction : ').split('/')
    f2=fraction(int(fn),int(fd))
    if choice==1:
        print(f1+f2)
    elif choice==2:
        print(f1-f2)
    elif choice==3:
        print(f1*f2)
    elif choice==4:
        print(f1/f2)
    elif choice==5:
        break
    else :
        print('Choose Between 1 and 4')
        
