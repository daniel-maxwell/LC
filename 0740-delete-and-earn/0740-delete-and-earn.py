class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        nums = list(set(nums))
        nums.sort()

        dp = [0] * len(nums)

        dp[0] = nums[0] * counts[nums[0]]

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                dp[i] = max(dp[i-1], dp[i-2] + (nums[i] * counts[nums[i]]))
            else:
                dp[i] = dp[i-1] + (nums[i] * counts[nums[i]])

        print(dp)

        return dp[-1]