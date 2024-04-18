class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [cost[0], cost[1]]
        steps = 2

        while steps < len(cost):
            tmp = min(minCost[0], minCost[1]) + cost[steps]
            minCost[0] = minCost[1]
            minCost[1] = tmp
            steps += 1

        return min(minCost[-1], minCost[-2])