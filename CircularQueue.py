class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None]*size
        self.front = self.rear = -1
        
    def enqueue(self, value):
        if((self.rear + 1) % self.size == self.front):
            print("Queue if full")
        elif self.front == -1: # Queue is empty
            self.front = self.rear = 0;
            self.items[self.rear] = value
            print(self.items)
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
            print(self.items)
    
    def dequeue(self):
        if(self.front == -1):
            print("Queue is empty")
        elif self.front == self.rear:
            print("Deleted item", self.items[self.front])
            self.front = self.rear - 1
            print(self.items)
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size
            print("Deleted item", self.items)
            

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
            