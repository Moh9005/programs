
def Paths(n, m):

    if (n == 0 or m == 0):
        return 1

    return (Paths(n - 1, m) + Paths(n, m - 1))



n =int(input("Enter X-cordinate = "))
m =int(input("Enter y-cordinate = "))
print(" Total number of paths are =", Paths(n, m))
