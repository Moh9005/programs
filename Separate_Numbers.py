input_string = input("Enter a list element of A separated by space = ")
a = input_string.split()
n=len(a)-1
x=[]
j=0
x.append(a[0])
sum=int(x[0])
for i in range(n):
    sum= sum+1
    x.append(str(sum))
if len(x) == len(a):
    for i in range(0, len(a)):
        if(a[i] == x[i]):
            j = j + 1
if(j==len(a)):
    print("GOOD STRING MATCH")
else:
    print("BAD MATCH")

