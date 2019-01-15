input_string = input("Enter a list element of A separated by space = ")
a = input_string.split()
x = input("Enter a list element of B separated by space =  ")
k=int(input("Enter the value of k = "))
b = x.split()
n=len(a)
count=0
a.sort(reverse = False)
b.sort(reverse = True)
for i in range(n):
    if(int(a[i])+int(b[i])>=k):
        count +=1
if(count==n):
    print("YES")
else:
    print("NO")




