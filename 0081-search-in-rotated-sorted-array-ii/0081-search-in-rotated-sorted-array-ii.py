class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) < 3:
            return True if target in nums else False

        SET = set(nums)

        return target in SET