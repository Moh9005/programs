def insert_element(a,x):
    return a.append(x)

def inorder(a):
    a.sort()
    return a

def postorder(a):
    a.sort(reverse=True)
    return a
def search(a,x):
    try:
       if a.index(x)!=None:
           print("index found")

    except ValueError:
        print("index not in the list")

input_string = input("Enter a list element separated by space = ")
a = input_string.split()

print("----------------------------------------------")
print("            OPREATIONS                        ")
print("----------------------------------------------")
print("                                              ")
print("For Insertion of an element:        Enter '1' ")
print("For InOrder traverse of an element: Enter '2' ")
print("For postOrder of an element:        Enter '3' ")
print("For binary Search of an element:    Enter '4' ")
print("                                              ")
print("----------------------------------------------")

print("                                              ")
x=input("Enter your choice for following opreations = ")

print("                                              ")
print("                                              ")
if x=='1':
    y= input("1- Insertion Selected:  Enter the element to last index of array = ")
    insert_element(a,y)
    print (a)

elif x=='2':
    print("inorder Sorting Selected")
    print("Old array ", a)
    print("Inorder Sorted Array =",inorder(a))
    print(x)
elif x=='3':
    print("Postorder Sorting Selected")
    print("Old array ", a)
    print("Postorder Sorted Array =", postorder(a))
elif x=='4':
    print("Binary search  Selected")
    q = input("Enter the element to search in array = ")
    search(a,q)