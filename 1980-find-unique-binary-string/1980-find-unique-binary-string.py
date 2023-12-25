class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        res = []

        def dfs(curr, i):
            nonlocal res
            
            if res: return

            if ''.join(curr) not in nums:
                res = curr.copy()
                return

            if i == n: return

            curr[i] = "1"
            dfs(curr, i+1)
            curr[i] = "0"
            dfs(curr, i+1)

        dfs(["0"]*n, 0)

        return ''.join(res)