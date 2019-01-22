input_string = input("Enter a list of strings separated by space = ")
a = input_string.split()
n=len(a)
for i in range(n):
    m = a.count(a[i])
    if m == 1:
        print("Non Repeatative Element = " ,a[i])
        break
if(m!=1):
    print(0," Non -Repeatative element")
