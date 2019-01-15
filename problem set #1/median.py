input_string = input("Enter a list element separated by space ")
list  = input_string.split()
list.sort()
n=len(list)
if n%2 == 0:
    median = int(list[int(n/2)])
else:
    median = int(list[int((n)/2)])

    print ('median =', median)

