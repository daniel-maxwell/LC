class ListNode:
    def __init__(self, key=-1, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> List Node
        self.leastRecentlyUsed = ListNode() # Linked list queue
        self.lruTail = self.leastRecentlyUsed # for evicting LRU key

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.useNode(self.cache[key])
            return self.cache[key].val
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.useNode(self.cache[key], value)
            
        else:
            newNode = ListNode(key, value)
            newNode.next = self.leastRecentlyUsed.next
            newNode.prev = self.leastRecentlyUsed

            if self.leastRecentlyUsed.next:
                self.leastRecentlyUsed.next.prev = newNode
            else:
                self.lruTail = newNode

            self.leastRecentlyUsed.next = newNode

            self.cache[key] = newNode
            
            if self.capacity == 0:
                self.cache.pop(self.lruTail.key)
                self.lruTail.prev.next = None
                self.lruTail = self.lruTail.prev
 
            else:
                self.capacity -= 1
            

    def useNode(self, node, newVal=None):
        
        if node == self.lruTail and self.lruTail.prev.key != -1:
            self.lruTail = self.lruTail.prev

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if newVal:
            node.val = newVal

        node.next = self.leastRecentlyUsed.next
        node.prev = self.leastRecentlyUsed

        if self.leastRecentlyUsed.next:
            self.leastRecentlyUsed.next.prev = node

        self.leastRecentlyUsed.next = node

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)