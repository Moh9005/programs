n=int(input("enter the value of n = "))
x=int(input("enter the value of x = "))
i=0
global m ,a,b
m=a=b=0
while (m<=n):
    m = m + x**i
    #print(m)
    if(m>n):
        m=a
        i=b
        print(x, "^", i, " + ")
        break;
    elif(m<=n):
        print(x, "^", i, " + ")
        a=m
        b=i
    elif(m!=n or m<n):
        print(x, "^", 0, " + ")


    i=i+1


