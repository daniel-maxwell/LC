class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curr, i):

            if i >= len(nums):
                res.append(curr.copy())
                return
            

            curr.append(nums[i])
            dfs(curr, i + 1)

            while i < len(nums) and nums[i] == curr[-1]:
                i += 1

            curr.pop()
            dfs(curr, i)

        dfs([], 0)

        return res