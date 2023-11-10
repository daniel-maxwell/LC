class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsCopy = nums.copy()

        k = k % len(nums)

        i, j = 0, len(nums) - k

        while i < len(nums):

            if j == len(nums):
                j = 0

            nums[i] = numsCopy[j]
            
            i += 1
            j += 1