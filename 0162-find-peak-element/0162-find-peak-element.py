class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while True:
            midIdx = low + (high - low)//2
            mid = nums[midIdx]
            left = nums[midIdx - 1] if midIdx - 1 >= 0 else float('-inf')
            right = nums[midIdx + 1] if midIdx + 1 < len(nums) else float('-inf')

            if left < mid and right < mid:
                return midIdx

            if left > mid:
                high = midIdx - 1

            elif right > mid:
                low = midIdx + 1

        return res