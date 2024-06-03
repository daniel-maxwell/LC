class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = [0] * (len(questions) + 1)

        for i in range(len(questions) -1, -1, -1):

            solveQ = questions[i][0]
            if i + questions[i][1] + 1 < len(dp):
                solveQ += dp[i + questions[i][1] + 1]

            skipQ = dp[i+1]

            dp[i] = max(solveQ, skipQ)

        return dp[0]    