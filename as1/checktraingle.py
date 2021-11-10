s0=float(input("side 1: "))
s1=float(input("side 2: "))
s2=float(input("side 3: "))
if(s0<s1+s2 and s1<s0+s2 and s2<s0+s1):
    print("Make Triangle")
else:
    print("Can't make triangle")