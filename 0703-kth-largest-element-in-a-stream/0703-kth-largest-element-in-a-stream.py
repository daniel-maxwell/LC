class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.heap = []
        self.k = k
        while nums and len(self.heap) < k:
            heapq.heappush(self.heap, nums.pop())


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        res = heapq.heappop(self.heap)
        heapq.heappush(self.heap, res)
        return res




        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)