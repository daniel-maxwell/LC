class MyHashSet:

    def __init__(self):
        self.Set = []
        

    def add(self, key: int) -> None:
        if key not in self.Set:
            self.Set.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.Set:
            self.Set.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.Set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)