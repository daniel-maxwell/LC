class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l, r = 0, n

        res = []

        while r < len(nums):
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r += 1

        return res