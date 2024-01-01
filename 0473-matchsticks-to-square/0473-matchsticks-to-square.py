class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        maxSL = sum(matchsticks) / 4
        if not maxSL.is_integer(): return False
        maxSL = int(maxSL)
        square = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if square[j] + matchsticks[i] <= maxSL:
                    square[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    square[j] -= matchsticks[i]
            return False

        return backtrack(0)