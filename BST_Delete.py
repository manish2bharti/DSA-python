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

def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root

        
def delete(root, value):
    if (root == None):
        return root
    if (root.data > value):
        root.left = delete(root.left, value)
    elif (root.data < value):
        root.right = delete(root.right, value) 
    else:
        if(root.left == None):
            return root.right
        
        if(root.right == None):
            return root.left
        
        else:
            successor = get_successor(root)
            root.data = successor.data
            root.right = delete(root.right, successor.data)
    return root
        

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

delete(root, 30)
print("/n")
inOrder(root)
