def getsum(n,l,u):
    # print(type(l,u))
    Sum = 0
    i = 0
    a = []
    while (i + l <= u):
        Sum += Sum + int(list[i + l])
        a.append(int(list[i + l]))
        i += 1
    print("Range Elements are ", a)
    print("Range sum =", sum(a))


input_string =input("Enter a list element separated by space ")
list  = input_string.split()
l = int(input("enter the lower range = " ))
u = int(input("enter the upper range = " ))
n=len(list)
getsum(n,l,u)