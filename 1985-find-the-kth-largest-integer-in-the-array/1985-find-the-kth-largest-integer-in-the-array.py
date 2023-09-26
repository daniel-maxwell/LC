class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(heapq.nlargest(k, list(map(int, nums)))[-1])