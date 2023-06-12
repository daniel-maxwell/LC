class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if prevMap.get(diff) is not None: return [prevMap[diff], i]
            else: prevMap[nums[i]] = i