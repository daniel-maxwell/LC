class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        while len(dp) < len(nums):
            dp.append(max(dp[-2] + nums[len(dp)], dp[-1]))

        return max(dp[-1], dp[-2])