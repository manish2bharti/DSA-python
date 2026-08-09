class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)

        if self.head != None:
            t1 = self.head

            while t1.next != None:
                t1 = t1.next

            t1.next = temp
        else:
            self.head = temp

    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertInMid(self, value, location):
        temp = Node(value)
        t1 = self.head

        while t1 != None:
            if t1.data == location:
                temp.next = t1.next
                t1.next = temp
                return

            t1 = t1.next

    def deleteLL(self, value):
        if self.head == None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        t1 = self.head.next

        while t1 != None:
            if t1.data == value:
                prev.next = t1.next
                return

            prev = t1
            t1 = t1.next

    def printLL(self):
        t1 = self.head

        while t1 != None:
            print(t1.data)
            t1 = t1.next


obj = SinglyLinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtBeg(15)
obj.insertAtEnd(30)
obj.insertInMid(40, 20)
obj.deleteLL(20)
obj.printLL()