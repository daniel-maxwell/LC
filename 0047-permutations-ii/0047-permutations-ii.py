class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def backtrack(lPos):
            if lPos == len(nums):
                return

            res.add(tuple(nums))

            for i in range(lPos + 1, len(nums)):
                nums[lPos], nums[i] = nums[i], nums[lPos]
                backtrack(lPos + 1)
                nums[lPos], nums[i] = nums[i], nums[lPos]
                backtrack(lPos + 1)           

        backtrack(0)

        return [list(tup) for tup in res]