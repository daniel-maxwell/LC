class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSeen = minSeen = res = nums[0]

        for i in range(1, len(nums)):
            temp = max(maxSeen * nums[i], minSeen * nums[i], nums[i])
            minSeen = min(maxSeen * nums[i], minSeen * nums[i], nums[i])
            maxSeen = temp
            res = max(res, maxSeen)

        return res