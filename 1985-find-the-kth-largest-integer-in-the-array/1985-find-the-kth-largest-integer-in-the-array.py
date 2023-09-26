class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(0, len(nums)):
            nums[i] = int(nums[i])
        return str(heapq.nlargest(k, nums)[-1])