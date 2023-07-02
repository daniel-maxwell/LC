class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0
        j = 0
        while i + j < l:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j += 1
            else:
                i += 1