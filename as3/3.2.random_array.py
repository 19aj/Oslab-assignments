from random import randint
n=randint(1,101)
numlis=[]
while len(numlis)!=n:
    el=randint(-10*n,10*n)
    if not el in numlis:
        numlis.append(el)
print("#Array Elements : ",len(numlis))
print("Random Array :\n",numlis)
        