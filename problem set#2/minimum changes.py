x=input("enter th string = ")
a=[]
n= len(x)
b=0
for i in range (n):
     if(a.count(x[i])==0):
         b =b+ (x.count(x[i])-1)
         a.append(x[i])
print(b, "number of changes are required")