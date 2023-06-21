class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)

        for i in range(0, len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum: return i
            else:
                leftSum += nums[i]
        return -1