# Python program to swap nodes

# A binary tree node
class Node:

    # constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
# Compare the new value with the parent node
        #if self.data:
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
def swap(root, level, k):


    if (root is None or (root.left is None and
                        root.right is None ) ):
        return

    # If current level+1 is present in swap vector
    # then we swap left and right node
    if (level+1)%k == 0:
        root.left, root.right = root.right, root.left

    # Recur for left and right subtree
    swap(root.left, level+1, k)
    swap(root.right, level+1, k)


def swapEveryKLevel(root, k):

    swap(root, 1, k)

# Method to find the inorder tree travesal
def inorder(root):

    # Base Case
    if root is None:
        return
    inorder(root.left)
    print (root.data,end=" ")
    inorder(root.right)

root = Node(1)
root.left=Node(2)
root.left.right=Node(4)
root.right=Node(3)
root.right.right=Node(5)

k = 2
print ("Before swap node :" )
inorder(root)

swapEveryKLevel(root, k)

print ("\nAfter swap Node : ")
inorder(root)
