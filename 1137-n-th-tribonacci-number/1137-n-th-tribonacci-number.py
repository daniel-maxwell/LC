class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1

        trib = [0, 1, 1]

        while len(trib) <= n:
            trib.append(trib[-3] + trib[-2] + trib[-1])

        return trib[-1]