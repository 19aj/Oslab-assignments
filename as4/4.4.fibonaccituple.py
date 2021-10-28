def recfibo(n):
    if n<=len(fibo)-1:
        return fibo[n]
    else:
        nextf=recfibo(n-2)+recfibo(n-1)
        fibo.append(nextf)
        return nextf
    
n=-1
fibo=[0,1]
while n<0 :
    n=int(input('n : '))
recfibo(n)
print(fibo[0:n+1])     # f0-fn
