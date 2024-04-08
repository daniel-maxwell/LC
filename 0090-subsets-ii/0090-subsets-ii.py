class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        added = set()

        def dfs(curr, i):
            if i == len(nums):
                x = curr.copy()
                x.sort()
                if tuple(x) not in added:
                    res.append(x)
                    added.add(tuple(x))
                return

            curr.append(nums[i])
            dfs(curr, i+1)
            curr.pop()
            dfs(curr, i+1)

        dfs([], 0)
        return res