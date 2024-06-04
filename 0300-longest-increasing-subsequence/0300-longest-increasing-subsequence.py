class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, currMax, res = [1], nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] > currMax:
                res += 1
                dp.append(res)
                currMax = nums[i]
                
            else:
                maxPrevStreak = 0
                for j in range(i-1, -1, -1):
                    if nums[j] < nums[i]:
                        maxPrevStreak = max(dp[j], maxPrevStreak)
                dp.append(1 + maxPrevStreak)
                if dp[-1] > res or dp[-1] == res and nums[i] < currMax:
                    res = dp[-1]
                    currMax = nums[i]
        return res