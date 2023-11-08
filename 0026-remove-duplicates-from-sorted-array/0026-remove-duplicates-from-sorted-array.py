class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)