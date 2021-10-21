n=int(input("# of Elements : "))
arr=[]
for i in range(0,n):
    print("Element [",i,'] : ',end=' ')
    arr.append(int(input()))
print(arr)
srt=True
for c in range(0,n-1):
    if arr[c]>arr[c+1]:
        srt=False
        break
if srt:
    print("Yes")
else :
    print("No")