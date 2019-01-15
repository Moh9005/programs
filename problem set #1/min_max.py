input_string = input("Enter a list element separated by space  ")
list  = input_string.split()
sum = 0
b=[]
for num in list:
    sum += int (num)
for i in range (len(list)):
    b.append (sum - int(list[i]))
print ("Maximum in array = ", max(b))
print ("Minimum in array = ", min(b))
