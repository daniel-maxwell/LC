class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [cost[0], cost[1]]

        i = 2

        while i < len(cost):
            minCost.append(min(minCost[i-1], minCost[i-2]) + cost[i])
            i += 1

        return min(minCost[-1], minCost[-2])