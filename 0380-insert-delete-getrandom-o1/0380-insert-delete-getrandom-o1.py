class RandomizedSet:

    def __init__(self):
        self.valsToIdx = {}
        self.valList = []

    def insert(self, val: int) -> bool:
        if val in self.valsToIdx:
            return False      
        else:
            self.valList.append(val)
            self.valsToIdx[val] = len(self.valList) -1
            return True
        
    def remove(self, val: int) -> bool:
        if val not in self.valsToIdx:
            return False
        
        else:
            if self.valList[-1] != val:
                self.valsToIdx[self.valList[-1]] = self.valsToIdx[val]
                self.valList[self.valsToIdx[val]] = self.valList[-1]
                self.valList.pop()

            else:
                self.valList.pop()

            self.valsToIdx.pop(val)
            return True
        
    def getRandom(self) -> int:
        return self.valList[random.randint(0, len(self.valList) -1)]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()