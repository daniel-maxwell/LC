class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daySet, dp = set(days), [0] * (days[0] - 1)
        minCostDay = min(costs)

        if minCostDay == costs[0]:
            dp.append(minCostDay)
        elif minCostDay == costs[1]:
            dp += [minCostDay] * 7
        else:
            dp += [minCostDay] * 30

        for i in range(len(dp) + 1, days[-1] + 1):
            if i not in daySet:
                dp.append(dp[-1])
                continue

            oneDay = costs[0] + dp[-1]

            sevenDay = costs[1]
            if i > 7:
                sevenDay += dp[-7]

            thirtyDay = costs[2]
            if i > 30:
                thirtyDay += dp[-30]

            dp.append(min([oneDay, sevenDay, thirtyDay]))

        return dp[-1]