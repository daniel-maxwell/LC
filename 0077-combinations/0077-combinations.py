class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(curr, i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i > n:
                return

            curr.append(i)
            i += 1
            dfs(curr, i)
            curr.pop()
            dfs(curr, i)

        dfs([], 1)
        return res