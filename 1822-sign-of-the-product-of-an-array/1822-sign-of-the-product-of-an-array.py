class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = nums[0]
        for i in range(1, len(nums)):
            product *= nums[i]
        if product == 0: return 0
        if product > 0: return 1
        else: return -1