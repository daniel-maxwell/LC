class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences = {}
        maxOccurrence = [nums[0],1]
        
        for i in range (0, len(nums)):   
            if nums[i] in occurrences:
                occurrences[nums[i]] += 1
                if occurrences[nums[i]] > maxOccurrence[1]:
                    maxOccurrence = [nums[i], occurrences[nums[i]]]
            else: occurrences[nums[i]] = 1
        
        return maxOccurrence[0]