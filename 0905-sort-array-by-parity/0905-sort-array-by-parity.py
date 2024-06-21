class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        odds, evens = 0, 0

        while odds < len(nums) and nums[odds] % 2 == 0:
            odds += 1

        while evens < len(nums) and nums[evens] % 2 == 1:
            evens += 1

        while evens < len(nums):
            res.append(nums[evens])
            evens += 1
            while evens < len(nums) and nums[evens] % 2 == 1:
                evens += 1

        while odds < len(nums):
            res.append(nums[odds])
            odds += 1
            while odds < len(nums) and nums[odds] % 2 == 0:
                odds += 1

        return res