class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        dp = [nums[0] * counts[nums[0]]]

        for i in range(1, len(nums)):
            curr = nums[i] * counts[nums[i]]

            if nums[i] - 1 not in counts:
                dp.append(dp[-1] + curr)

            else:
                skipCurrent = (dp[-2] if i >= 2 else 0) + curr
                dp.append(max(dp[-1], skipCurrent))
        
        return dp[-1]