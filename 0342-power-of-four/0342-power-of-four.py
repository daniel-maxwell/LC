class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        if n <= 0: return False
        n, x = abs(n), 1
        while 4 ** x < n: x += 1
        return True if 4 ** x == n else False