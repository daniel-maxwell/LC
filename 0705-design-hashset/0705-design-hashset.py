class MyHashSet:

    def __init__(self):
        self.Set = []
        self.log = {}
        

    def add(self, key: int) -> None:
        if self.log.get(key) is None:
            self.Set.append(key)
            self.log[key] = len(self.Set) -1
        

    def remove(self, key: int) -> None:
        if self.log.get(key) is not None:
            self.Set[self.log[key]] = -1
            del self.log[key]
        

    def contains(self, key: int) -> bool:
        return self.log.get(key) is not None
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)