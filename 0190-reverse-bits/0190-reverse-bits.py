class Solution:
    def reverseBits(self, n: int) -> int:
        temp = bin(n)[:1:-1]

        while len(temp) != 32:
            temp = temp + '0'

        return int(temp, 2)