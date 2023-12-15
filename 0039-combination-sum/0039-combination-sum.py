class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(currList, currSum, i):
            if currSum > target:
                return
            elif currSum == target:
                res.append(currList.copy())
                return
            elif i == len(candidates):
                return

            currList.append(candidates[i])
            currSum += candidates[i]
            dfs(currList, currSum, i)

            currSum -= currList.pop()
            dfs(currList, currSum, i + 1)

        dfs([], 0, 0)

        return res