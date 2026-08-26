class Node:
    def __init__(self, value):
        self.left = None
        self.right= None
        self.data = value
        
def insert(root, value):
    if (root == None):
        return Node(value)
    
    if (root.data == value):
        return root
    
    if (root.data > value):
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value) 
    return root

def search(root, value):
    if (root == None):
        print(f"\nElement {value} not found")
        return
    
    if (root.data == value):
        print(f"\nElement {value} found")
        return
    
    if (root.data > value):
        search(root.left, value)
    else:
        search(root.right, value) 

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")    
        inOrder(root.right) 
    
root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

print("\nInOrder Traversal")
inOrder(root)
search(root, 12)
search(root, 19)