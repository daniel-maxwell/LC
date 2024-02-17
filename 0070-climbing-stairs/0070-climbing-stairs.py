class Solution:
    def climbStairs(self, n: int) -> int:
        totalWays = [1, 2, 3]

        if n <= 3:
            return totalWays[n-1]

        else:
            while len(totalWays) < n:
                totalWays.append(totalWays[-1] + totalWays[-2])

            return totalWays[-1]