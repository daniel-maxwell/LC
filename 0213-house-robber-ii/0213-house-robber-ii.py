class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        return max(self.get(nums, 0, 1, len(nums) - 1), self.get(nums, 1, 2, len(nums)))

    def get(self, nums: List[int], a: int, b: int, c: int) -> int:
        maxCash = [nums[a], max(nums[a], nums[b])]

        i = b + 1
        while i < c:
            tmp = maxCash[-1]
            maxCash[-1] = max(nums[i] + maxCash[0], maxCash[-1])
            maxCash[0] = tmp
            i += 1

        return maxCash[-1]