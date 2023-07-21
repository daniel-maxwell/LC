class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        l, r, x = 0, len(nums) -1, len(nums) -1
        
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res[x] = nums[l] ** 2
                l += 1
            else:
                res[x] = nums[r] ** 2
                r -= 1
            x -= 1
 
        return res
            