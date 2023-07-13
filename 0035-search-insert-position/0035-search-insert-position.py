class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        m = math.floor(r/2)

        for i in range(0, math.floor(math.log2(len(nums)))):
            if nums[m] < target:
                l = m
            elif nums[m] > target:
                r = m
            else:
                return m
            m = math.floor((l+r)/2)

        if nums[m] > target:
            return max(0, m)
        elif nums[m] < target:
            return min(len(nums), m+1)
        else: return m