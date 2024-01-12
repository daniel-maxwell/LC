class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')

        currSum = nums[0]
        l, r = 0, 1

        while l < len(nums):
            if currSum >= target:
                if r - l < minLength:
                    minLength = r - l
                currSum -= nums[l]
                l += 1

            elif r < len(nums):
                currSum += nums[r]
                r += 1
            
            else:
                break

        return minLength if minLength <= len(nums) else 0