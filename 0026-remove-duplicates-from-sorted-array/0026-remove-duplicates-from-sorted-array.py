class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idxStack = []
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                idxStack.append(i)

        while idxStack:
            nums.pop(idxStack.pop())

        return len(nums)