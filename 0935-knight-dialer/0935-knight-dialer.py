class Solution:
    def knightDialer(self, n: int) -> int:

        if n == 1:
            return 10

        possibleMoves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        mod = 10**9 + 7
        dp = [1] * 10

        for _ in range(n-1):
            newDP = [0] * len(dp)
            for i in range(len(dp)):
                for move in possibleMoves[i]:
                    newDP[i] += dp[move]
            dp = newDP
        return sum(dp) % mod