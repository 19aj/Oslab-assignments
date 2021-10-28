def checkered(r,c):
    x=0
    for i in range(0,r):
        for j in range(0,c):
            if x:    
                print('*',end='')
                x=0
            else :
                print('#',end='')
                x=1
                
        print()
        if j%2!=0:
            if x:
                x=0
            else :
                x=1

m,n=0,0
while n<=0 or m<=0:
    n=int(input('Row : '))
    m=int(input('Column : '))
checkered(n,m)
    