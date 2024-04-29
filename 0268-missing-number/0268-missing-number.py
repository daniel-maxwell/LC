class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        XORi, XORnums = 0, 0

        for i in range(0, len(nums)):
            XORi ^= i
            XORnums ^= nums[i]

        XORi ^= len(nums)

        return XORi ^ XORnums
