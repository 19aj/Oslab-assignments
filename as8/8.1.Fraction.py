from math import gcd

class Fraction:
    def __init__(self,numerator,denominator):
        self.n=numerator
        self.d=denominator
    def __add__(self,of):
        if self.d==of.d:
            return Fraction(self.n+of.n , of.d)
        else :
            return Fraction(self.n*of.d + self.d*of.n , self.d*of.d)
    def __sub__(self,of):
        if self.d==of.d:
            return Fraction(self.n-of.n , of.d)
        else :
            return Fraction(self.n*of.d - self.d*of.n , self.d*of.d)
    def __mul__(self,of):
        return Fraction(self.n*of.n , self.d*of.d)
    def __truediv__(self,of):
        return Fraction(self.n*of.d , self.d*of.n)
    def simplify_fraction(self):
        self.n=self.n//gcd(self.n,self.d)
        self.d=self.d//gcd(self.n,self.d)
        return self
    def __str__(self):
        return str(self.n)+'/'+str(self.d)
    
while True:
    print('1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Simplify\n6.Exit')
    choice=int(input('Chioce : '))
    if choice==1:
        fn,fd=input('First Fraction : ').split('/')
        f1=Fraction(int(fn),int(fd))
        fn,fd=input('Second Fraction : ').split('/')
        f2=Fraction(int(fn),int(fd))
        print(f1+f2)
    elif choice==2:
        fn,fd=input('First Fraction : ').split('/')
        f1=Fraction(int(fn),int(fd))
        fn,fd=input('Second Fraction : ').split('/')
        f2=Fraction(int(fn),int(fd))
        print(f1-f2)
    elif choice==3:
        fn,fd=input('First Fraction : ').split('/')
        f1=Fraction(int(fn),int(fd))
        fn,fd=input('Second Fraction : ').split('/')
        f2=Fraction(int(fn),int(fd))
        print(f1*f2)
    elif choice==4:
        fn,fd=input('First Fraction : ').split('/')
        f1=Fraction(int(fn),int(fd))
        fn,fd=input('Second Fraction : ').split('/')
        f2=Fraction(int(fn),int(fd))
        print(f1/f2)
    elif choice==5:
        fn,fd=input('Fraction : ').split('/')
        f1=Fraction(int(fn),int(fd))
        f1.simplify_fraction()
    elif choice==6:
        break
    else :
        print('Choose Between 1 and 6')
        
