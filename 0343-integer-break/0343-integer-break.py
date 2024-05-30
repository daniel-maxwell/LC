class Solution:
    def integerBreak(self, n: int) -> int:
        a = 1
        while n > 10:
            n -= 3
            a *= 3

        b = 0
        def dfs(nums, remaining):

            if remaining == 0:
                if len(nums) > 1:
                    nonlocal b
                    x = 1
                    for num in nums:
                        x *= num
                    b = max(b, x)
                return

            
            for i in range(1, remaining + 1):
                nums.append(i)
                remaining -= i
                dfs(nums, remaining)
                remaining += nums.pop()
        
        dfs([], n)
        return a * b