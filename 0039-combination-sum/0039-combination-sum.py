class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        added = set()

        def dfs(curr, i, currSum):

            if currSum == target:
                if tuple(curr) not in added:
                    result.append(curr.copy())
                    added.add(tuple(curr))
                
            if currSum > target or i == len(candidates):
                return

            currSum += candidates[i]
            curr.append(candidates[i])
            dfs(curr, i, currSum)
            currSum -= curr.pop()
            dfs(curr, i+1, currSum)

        dfs([], 0, 0)
    
        return result