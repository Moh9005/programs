input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print("sum of elements in list")
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)
