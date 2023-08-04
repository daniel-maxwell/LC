class MinStack:

    def __init__(self):
        self.stack = []
        self.minMap = {}
        self.minVal = math.inf
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minVal > val:
            if len(self.minMap) == 0:
                self.minVal = val
                self.minMap[val] = {math.inf: 1}
            else:
                self.minMap[val] = {self.minVal: 1}
                self.minVal = val

        elif val in self.minMap:
            toUpdate = list(self.minMap[val].keys())[0]
            self.minMap[val][toUpdate] += 1
        
        else:
            self.minMap[val] = {self.minVal: 1}


    def pop(self) -> None:

        if self.top() == self.minVal:
            minValdict = list(self.minMap[self.minVal].items())

            if minValdict[0][1] == 1:
                self.minVal = minValdict[0][0]
                self.minMap.pop(self.stack[-1])
            else:
                self.minMap[self.minVal][minValdict[0][0]] -= 1
            
        else:
            popValdict = list(self.minMap[self.top()].items())

            if popValdict[0][1] == 1:
                self.minVal = popValdict[0][0]
                self.minMap.pop(self.top())
            else:
                self.minMap[self.top()][popValdict[0][0]] -= 1

        self.stack.pop()
    

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal
            

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()