
#input_string =input("Enter a list element separated by space ")
#list=input_string.split()
list = [5,0,10,2,4,1,6]
i=j=count=0
n=len(list)
print("ordered pairs are =")
for i in range (n):
    for j in range (n):
        if (i <j and ((i* int(list[i])) > (j * int(list[j]) ))):
            print("(",int(list[i]),",",int(list[j]),")" )
            count += 1
print("total number of ordered Pairs = ",count)