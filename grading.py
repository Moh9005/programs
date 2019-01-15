input_string = input("Enter a list element separated by space ")
x = input_string.split()
i=0
global a
a=0
n=len(x)
print("Old string  = ",x)
while(i<n and int(x[i])>=38):
    if(int(x[i])%5!=0):
        a= 5 * ( int(int(x[i])/5)+ 1)
        y = a - int(x[i])
        if y < 3 :
            x[i]=str(a)
            i=i+1
        else:
            i=i+1
print("Rounded off string  = ",x)
