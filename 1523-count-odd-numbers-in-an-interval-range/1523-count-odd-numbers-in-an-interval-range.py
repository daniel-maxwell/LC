class Solution:
    def countOdds(self, low: int, high: int) -> int:
        add = 1 if low % 2 == 1 or high % 2 == 1 else 0
        return ((high - low) // 2) + add
