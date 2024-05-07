class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]

        for i in range(2, n):
            temp = ways[0] + ways[1]
            ways[0], ways[1] = ways[1], temp

        return ways[-1] if n > 1 else ways[0]