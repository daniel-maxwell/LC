class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0

        while n >= 0:

            rows += 1
            n -= rows
            if n < 0:
                return rows - 1
        
        return rows