input_string = input("Enter a list of strings separated by space = ")
a = input_string.split()
n=len(a)
b=[]
i=1
for i in range(1,n+1):
    b.append((a.count(str(i))))
print("Frequency of Each Element = ",b)