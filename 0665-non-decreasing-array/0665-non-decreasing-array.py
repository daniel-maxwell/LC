class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True

        changes = None
        
        if nums[0] < nums[1]:
            changes = 0
        else:
            if nums[0] <= nums[2]: nums[1] = nums[2]
            else: nums[0] = nums[1]
            changes = 1

        for i in range(1, len(nums)):
            prev = nums[i-1]

            if nums[i] < prev:

                if i == len(nums) - 1:
                    return changes + 1 < 2

                if i+1 < len(nums) and prev <= nums[i+1]:
                    nums[i] = prev

                else:
                    nums[i-1] = nums[i]
                    if i - 2 >= 0 and nums[i-2] > nums[i-1]:
                        return False

                changes += 1

            if changes > 1:
                return False

        return True