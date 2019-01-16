a=[]
b=[]
class Node:
    def __init__(self,data):
        self.data=data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert ( self,newNode):
        if self.head is None:

            self.head =newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next=newNode
        a.append(hex(id(newNode)))
    def printList(self):

        if self.head is None:
            print("the list is empty")
            return
        currentNode = self.head
        while True:

            if currentNode is None:
                break
            print(currentNode.data)

            currentNode = currentNode.next

    def delete(self):
         lastNode = self.head

         while lastNode.next is not None:
             previousNode=lastNode
             lastNode=lastNode.next
         previousNode.next=None


firstNode= Node("John")

LinkedList=LinkedList()

LinkedList.insert(firstNode)

SecondNode= Node("ben")
LinkedList.insert(SecondNode)

thirdNode= Node("scot")
LinkedList.insert(thirdNode)
LinkedList.printList()
#print(a)
n=len(a)
for i in range (n):
    l=a.count(a[i])
if(l>1):
    print("cycle is present")
else:
    print("cycle is absent")
#print(a[0].data)