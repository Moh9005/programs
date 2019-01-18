
input_string =input("Enter a list element separated by space ")
list=input_string.split()
i=j=count=0
n=len(list)
for i in range (n):
    for j in range (n):
        if (i* int(list[i])) > (j * int(list[j])):
            print(i,j,list[i],list[j])
            count += 1
print(count)