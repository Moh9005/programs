a=input("enter string # 1 ")
b=input("enter string # 2 ")
n=len(a)
x=len(b)
c=[]
global m
m=0
i=j=0
for i in range (n):
    for j in range (x):
        # print(b[j], c[l] ,j,l)
        if a[i]==b[j]:
            #c.append(a[i])
            m +=1
print(c)

if(m==0):
    print("no match found")
else:
    print("match found")
