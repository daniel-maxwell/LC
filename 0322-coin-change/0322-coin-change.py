class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()
        coinSet = set(coins)

        for i in range(1, len(dp)):
            if i in coinSet:
                dp[i] = 1
                continue
            MIN = float('inf')
            for coin in coins:
                if coin > i:
                    break
                MIN = min(MIN, 1 + dp[i - coin])
            dp[i] = MIN

        return dp[-1] if dp[-1] != float('inf') else -1