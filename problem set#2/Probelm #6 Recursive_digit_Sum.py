def sum(x):#Sum Function
    count=0
    for i in str(x):
        count +=ord(i) - 48
    #print('Count: ', count)
    return count

def recursive_Sum (a):#Recursive Function
    if (len(a)==1):
        return a
    else:
        m=sum(a)
        return recursive_Sum(str(m))


st=input("Enter a string =")# Main Function
n=input("No of times to repeat:")
x=st * int(n)
l=recursive_Sum (x)
print("Super digit = ",l)
