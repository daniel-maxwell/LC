class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low -= low % 2
        high += high % 2
        return math.floor((high - low) / 2)