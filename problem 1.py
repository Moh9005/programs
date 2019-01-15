import math
n=int(input("enter the value of n = "))
x=int(input("enter the value of d = "))
global m
global a
m=0
i=0
a=0
j=0
while ( a<=x ):
        a = math.pow(2,j)
        if (a == x):
            print( " factors  are 2 ^ " , j )
            while (m <= n):
                m = math.pow(x,i)
                if (m == n):
                    print( " factors  are ",x, " ^ " , i )
                    print("output =yes")
                    break;

                i=i+1

        j=j+1


