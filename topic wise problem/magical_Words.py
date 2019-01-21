t= int(input("Enter the Number Of Testcases = "))
x=[]

for i in range (t):
    x=input("Enter the string = ")
    n=len(x)
    b=[]
    for i in range (n):
        b.append(chr(123-(26-(122 - ord(x[i])))))
    print ("Magical string = ","".join(map(str,b)))