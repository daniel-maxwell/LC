class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        n = str(bin(n))

        for i in range(2, len(n)):
            counter += int(n[i])

        return counter