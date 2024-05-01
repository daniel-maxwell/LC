class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i + j < len(nums:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j += 1
            else:
                i += 1
