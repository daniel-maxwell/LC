class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        res = 0
        for dig in n:
            if dig == '1': res += 1

        return res
        