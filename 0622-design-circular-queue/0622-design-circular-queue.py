# [[8],[3],[9],[5],[0],[],[],[],[],[],[],[]]
# ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.currLength = 0
        self.maxLength = k
        self.head = None
        self.tail = None
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        new = ListNode(value)

        if self.currLength == 0: # Empty list
            new.next = self.head
            self.head = new
            self.tail = new
        
        elif self.currLength == 1: # One element
            self.head.next = new
            self.tail = new
            self.tail.next = self.head

        else:                      # Many elements
            new.next = self.head
            self.tail.next = new
            self.tail = new

        self.currLength += 1
        return True

        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.currLength == 1:
            self.head, self.tail = None, None
            
        else:
            self.tail.next = self.head.next
            self.head = self.head.next

        self.currLength -= 1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.val
        

    def isEmpty(self) -> bool:
        if self.currLength == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.currLength == self.maxLength:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()