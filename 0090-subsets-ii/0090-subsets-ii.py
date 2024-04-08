class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curr, i):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(curr, i+1)
            val = curr.pop()
            while i < len(nums) and nums[i] == val:
                i += 1
            dfs(curr, i)

        dfs([], 0)
        return res