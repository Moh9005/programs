input_string = input("Enter a list element separated by space = ")
x = input_string.split()
k=int(input("Enter the value of K = "))
n=len(x)
global count
global a
count =0
i=0
a = 1
for i in range (n):
    if(i<a and a<=n):
        for a in range (n):
            #print(i,a)
            m=int(x[i])+ int(x[a])
            #print(i,a,x[i], x[a],m)
            if(i<a and m%k==0):
                count +=1
            a=a+1
    i=i+1
print(count)
