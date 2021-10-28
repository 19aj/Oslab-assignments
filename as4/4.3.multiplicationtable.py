def multable(r,c):
    r+=1
    c+=1
    print(end='\t')
    for k in range(1,c):
        print(k,end='\t')
    print('\n')
    for i in range(1,r):
        print(i,end='\t')
        for j in range (1,c):
            print(i*j,end='\t')
        print()
        
m,n=0,0
while n<=0 or m<=0:
    n=int(input('Row : '))
    m=int(input('Column : '))
multable(n,m)