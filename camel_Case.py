x = input("Enter a list element separated by space ")
n=len(x)-1
count=1
for i in range(n):
    y = x[i].isupper()
    #print(i)
    if(y==True):
        count +=1
print("total number of Words ",count)

