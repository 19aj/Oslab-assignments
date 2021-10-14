sec=input("second : ")
t0=int(sec)//3600
t1=int(sec)%3600//60
t2=int(sec)%60
print(str(t0).zfill(2),':',str(t1).zfill(2),':',str(t2).zfill(2),':')
