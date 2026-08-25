class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self, value):
        self.items.append(value)
        print(self.items)
    
    def insertAtFront(self, value):
        self.items.insert(0, value)
        print(self.items)
        
    def deleteAtFront(self):
        if self.isEmpty(): 
            print("Queue is empty")
        else: 
            print(self.items)
            return self.items.pop(0)
            
    def deleteAtEnd(self):
        if self.isEmpty(): 
            print("Queue is empty")
        else: 
            print(self.items)
            return self.items.pop()
            
        
            
q = Deque()
q.insertAtEnd(10)
q.insertAtFront(20)
q.insertAtEnd(30)
q.insertAtEnd(40)
q.insertAtFront(50)
q.deleteAtEnd()
q.deleteAtEnd()
q.deleteAtFront()
q.deleteAtFront()
q.deleteAtEnd()
q.deleteAtFront()