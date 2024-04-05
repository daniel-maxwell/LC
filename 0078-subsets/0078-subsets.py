class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, curr, res):
            if i >= len(nums):
                return

            curr.append(nums[i])
            dfs(i+1, curr, res)
            res.append(curr.copy())
            curr.pop()
            dfs(i+1, curr, res)
            
            return res

        res = [[]] + (dfs(0, [], []))

        return res