class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = [n for n in nums]
        self.k = k
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > k:
            heapq.heappop(self.maxHeap)

    def add(self, val: int) -> int:
        if len(self.maxHeap) < self.k:
            heapq.heappush(self.maxHeap, val)
            return self.maxHeap[0]

        elif val > self.maxHeap[0]:
            heapq.heappushpop(self.maxHeap, val)
            return self.maxHeap[0]

        else:
            return self.maxHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)