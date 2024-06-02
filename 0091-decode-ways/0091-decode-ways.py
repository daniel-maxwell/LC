class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        
        for i in range(len(dp)-2, -1, -1):

            single = int(s[i])
            double = int(s[i:i+2]) if i < len(s) - 1 else None

            if single == 0:
                if i > 0 and 0 < int(s[i-1]) < 3:
                    continue
                else:
                    return 0

            else:
                dp[i] += dp[i+1]


            if double and double <= 26:
                dp[i] += dp[i+2]

        return dp[0]
