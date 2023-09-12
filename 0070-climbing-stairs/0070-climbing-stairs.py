class Solution:
    def climbStairs(self, n: int) -> int:
        
        steps = [1, 2, 3]

        if n <= len(steps):
            return steps[n-1]

        for i in range(2, n-1):
            steps.append(steps[-1] + steps[-2])

        return steps[-1]      