class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = {nums[0]:1}
        maxEl = nums[0]

        if len(nums) < 2:
            return maxEl

        for num in nums[1:]:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1

            if occurences[num] > occurences[maxEl]:
                maxEl = num

        return maxEl