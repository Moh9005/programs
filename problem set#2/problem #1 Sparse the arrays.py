input_string = input("Enter a list of strings separated by space = ")
a = input_string.split()
x = input("Enter a list  of queries separated by space =  ")
b = x.split()
n=len(b)
c=[]
for i in range(n):
    c.append(a.count(b[i]))
print("Resultant array =  ",c)

