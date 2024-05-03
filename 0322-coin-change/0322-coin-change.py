class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coinSet = set(coins)

        for i in range(1, len(dp)):

            if i in coinSet:
                dp[i] = 1
                continue

            for c in range(len(coins) -1, -1, -1):
                if coins[c] > i:
                    continue

                if dp[i - coins[c]] != float('inf'):
                    dp[i] = min(dp[i - coins[c]] + 1, dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1    