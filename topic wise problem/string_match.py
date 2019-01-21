a=input("enter string # 1 ")
b=input("enter string # 2 ")
n=len(a)
x=len(b)
c=[]
global m
m=0
i=j=0
for i in range (n):
    try:
        x = b.index(a[i])
        if(x is not None):
            print(" match found")
            break
    except Exception:
        m +=1

if m==n:
    print("No match found")