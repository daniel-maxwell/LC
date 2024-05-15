class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = {}
        k, i = 0, 0
        while i < len(nums):
            if counts.get(nums[i], 0) == 2:
                nums.pop(i)
                i -= 1
                
            else:
                if nums[i] in counts:
                    counts[nums[i]] += 1
                else:
                    counts[nums[i]] = 1
                k += 1
            i += 1
        return k + 1