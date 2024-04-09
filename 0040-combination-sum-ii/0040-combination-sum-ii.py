class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(curr, currSum, i):

            if currSum == target:
                res.append(curr.copy())
                return

            if i == len(candidates) or currSum > target:
                return

            curr.append(candidates[i])
            currSum += candidates[i]
            backtrack(curr, currSum, i + 1)
            while i < len(candidates) and candidates[i] == curr[-1]:
                i += 1
            currSum -= curr.pop()
            backtrack(curr, currSum, i)

        backtrack([], 0, 0)
        return res