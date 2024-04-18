class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]

        while n > 2:
            tmp = ways[-1]
            ways[-1] += ways[-2]
            ways[-2] = tmp
            n -= 1

        return ways[-1] if n == 2 else ways[0]