class Solution:
    def numSquares(self, n: int) -> int:

        dp = [0,1,2,3,1]

        perfectList = [1, 4]

        if n < len(dp):
            return dp[n]

        i = 5
        while i <= n:
            sqrt_i = int(math.sqrt(i))
            if sqrt_i * sqrt_i == i:
                perfectList.append(i)
                dp.append(1)

            else:
                minSqrs = float('inf')
                for num in perfectList:
                    minSqrs = min(minSqrs, 1 + dp[i - num])
                dp.append(minSqrs)
            i += 1

        return dp[-1]