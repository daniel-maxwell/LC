class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        days_set = set(days)

        for i in range(1, len(dp)):
            if i not in days_set:
                dp[i] = dp[i-1]
                continue

            cost1 = dp[i - 1] + costs[0]
            cost7 = dp[i - 7] + costs[1] if i >= 7 else costs[1]
            cost30 = dp[i - 30] + costs[2] if i >= 30 else costs[2]

            dp[i] = min(cost1, cost7, cost30)

        return dp[-1]