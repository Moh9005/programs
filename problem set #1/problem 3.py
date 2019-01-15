import math
n=int(input("enter the value  = "))
i = 1
total = 2
while (i <= n):
    if (n % total != 0):
        total =total+1
        i = 1
        continue;

    else:

        global m
        m = math.pow(total,i)
        if (m == n):
            print( " factors  are ",total, " ^ " , i )
            print("output true")
            break;

        elif (m > n):
            total = total + 1
            i = 1
            m = 0
            continue
    i=i+1
