class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [1]

        '''
        We use previously computed results to compute the number of combinations which sum to i

        for each num that we're given, we can get the number of combinations that we can add num to
        to get i from dp[i - num]. Iterating through nums and adding these results to dp[i]
        gets up the number of combinations we can use to get i
        '''

        for i in range(1, target + 1):
            combinations = 0
            for num in nums:
                if num <= i:
                    combinations += dp[i - num]

            dp.append(combinations)

        return dp[-1]