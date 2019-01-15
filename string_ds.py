a=input("enter string # 1 ")
b=input("enter string # 2 ")
n=len(a)-1
x=len(b)-1
c=[]
global m
m=0
i=j=0
while (i!=n and j!=x):
    if(a[i]== b[j]):
       c.append(a[i])
       i=i+1
       m=m+1
       print('output = yes ')
    elif(a[i]!= b[j]):
        j=j+1
        i=i+1
if(m==0):
    print("no match found")

