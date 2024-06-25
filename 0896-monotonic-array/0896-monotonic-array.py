class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if direction == 0:
                        return False
                else:
                    direction = 1

            elif nums[i] < nums[i-1]:
                if direction == 1:
                        return False
                else:
                    direction = 0
        return True