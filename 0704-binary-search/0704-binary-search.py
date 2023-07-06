class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target in nums: return 0
            else: return -1
        
        mid = math.floor(len(nums)/2)
        buffer = mid

        for count in range(0, math.floor(len(nums)/2) + 1):
            if nums[mid] == target: return mid
            if nums[mid] > target: mid = math.floor(mid/2)
            else:
                buffer = max(math.floor(buffer/2), 1)
                mid = min(mid + buffer, len(nums)-1)
        return -1