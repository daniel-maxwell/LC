class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        res = [None]*len(nums)
        l = len(nums)
        median = nums[l//2] if l % 2 else (nums[(l//2) - 1] + nums[(l//2)]) / 2

        resIdx = 1
        for i in range(0, len(nums)//2):
            res[resIdx] = nums[i]
            resIdx += 2

        resIdx = 0

        for i in range(len(nums)//2, len(nums)):
            res[resIdx] = nums[i]
            resIdx += 2

        return res