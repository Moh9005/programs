
def takefirst(elem):
    return elem[0]

# the first line of input is the number of rows of the array
n = int(input())
a = []
for i in range(n):
    a.append([(j) for j in input().split()])
b=[]
for i in range(int(n/2)):
    a[i][1] = '-'

a.sort(key=takefirst)

#print(a)
for j in range (n):
    b.append(a[j][1])

print (" ".join(map(str,b)))


