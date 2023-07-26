class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                r += 1
            elif nums[i] == 1:
                w += 1
            else: 
                b += 1

        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:] = [2] * b

        return nums