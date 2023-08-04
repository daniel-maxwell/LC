class MyStack:

    def __init__(self):
        self.inQueue = []
        self.outQueue = []   

    def push(self, x: int) -> None:
        self.outQueue.append(x)
        self.inQueue.insert(0, x)

    def pop(self) -> int:
        self.inQueue.pop(0)
        return self.outQueue.pop()

    def top(self) -> int:
        return self.inQueue[0]
        

    def empty(self) -> bool:
        return len(self.inQueue) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()