n = int(input("enter the number of elements in an array =  "))
k = int(input("enter the number of left rotations of an array =  "))
a=[]
for i in range (n):
    a.append(int(input("enter the value of index ")))

b = []
i = 0
while (i < n):
    if (i + k) <= (n - 1):
            b.append(a[i+k])
    elif (i+k-n) < (n-1):
            b.append(a[i+k-n])
    i = i+1
print(b)
