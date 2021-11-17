from random import randint
boys=['ali','reza','yasin','benyamin','mehrdad','sajad','aidin','shahin']
girls=['sara','zari','neda','homa','eli','goli','mary','mina']
ob=[]
og=[]
while len(ob)<len(boys):
    r1=randint(0,len(boys)-1)
    if r1 not in ob:
        ob.append(r1)
    r2=randint(0,len(girls)-1)
    if r2 not in og:
        og.append(r2)
        
boys=[boys[i] for i in ob ]
girls=[girls[i] for i in og ]
resault=list(zip(boys,girls))
print(resault)