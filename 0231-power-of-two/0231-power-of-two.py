class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        val = 2**power

        while val <= n:
            if val == n:
                return True
            power += 1
            val = 2 ** power

        return False 
        