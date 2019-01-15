m = int(input("Enter a list element separated by space  "))
x=str(m)
n=len(x)
i=0
global a
a=0
while(i<n):
    try:
        if(m % int(x[i]) ==0):
            print(x[i]," is divisor of ",m)
            a=a+1
        else:
            print(x[i]," is not divisor of ",m)
    except ZeroDivisionError:
        print(x[i]," is undefined")
    i=i+1
print(a ," total number of digits are divisible")
