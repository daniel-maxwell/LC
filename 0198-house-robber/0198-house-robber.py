class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxCash = [nums[0], max(nums[0], nums[1])]

        i = 2

        while i < len(nums):
            tmp = maxCash[-1]
            maxCash[-1] = max(maxCash[-2] + nums[i], maxCash[-1])
            maxCash[-2] = tmp
            i += 1
        
        return maxCash[-1]