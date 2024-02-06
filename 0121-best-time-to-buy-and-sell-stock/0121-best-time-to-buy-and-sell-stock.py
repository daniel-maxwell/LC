class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        l, r = 0, 1

        def profit(a, b):
            return b - a

        priceRanges = [[0, 0] for _ in range(len(prices))]

        MIN = float('inf')
        
        for i in range(len(prices)):
            MIN = min(prices[i], MIN)
            priceRanges[i][0] = MIN

        MAX = float('-inf')
        for i in range(len(prices)-1, -1, -1):
            MAX = max(prices[i], MAX)
            priceRanges[i][1] = MAX

        res = profit(priceRanges[0][0], priceRanges[0][1])

        for rng in priceRanges:
            res = max(profit(rng[0], rng[1]), res)

        return max(res, 0)