input_string = input("Enter a list element of A separated by space = ")
a = input_string.split()
x=len(a)
n=int(len(a)/2)
b=[]
c=[]
l=j=0
count=0
print(a)
if(x%2==0):
    for i in range (n):
        b.append(a[i])
        c.append(a[i+n])
    for j in range (n):
        for l in range (n):
        # print(b[j], c[l] ,j,l)
            if b[j]==c[l]:
                c[l]= ' '
                count +=1
    f=c.count(' ')
    print (n-f," Changes Required ")
else:
    print(-1, "NOT POSSIBLE")





