x=input("time : ")

t0 ,t1 ,t2 = x.split(':')

ans=int(t0)*60*60 + int(t1)*60 + int(t2) 
print(ans)