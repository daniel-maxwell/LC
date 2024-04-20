class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.get(nums[1:]), self.get(nums[:-1]))

    def get(self, nums: List[int]) -> int:
        

        maxCash = [nums[0], max(nums[0], nums[1])]

        i = 2
        while i < len(nums):
            tmp = maxCash[-1]
            maxCash[-1] = max(nums[i] + maxCash[0], maxCash[-1])
            maxCash[0] = tmp
            i += 1

        return maxCash[-1]