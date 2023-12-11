class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        lengthToCounts, i = {}, 0

        # Populates dict
        while i < len(nums):
            l = i
            while i < len(nums) and nums[i] == 0:
                i += 1

            if i != l:
                if i - l in lengthToCounts:
                    lengthToCounts[i - l] += 1
                else:
                    lengthToCounts[i - l] = 1
            i += 1

        res = 0

        for length, occ in lengthToCounts.items():
            res += (length * (length + 1)//2) * occ

        return res