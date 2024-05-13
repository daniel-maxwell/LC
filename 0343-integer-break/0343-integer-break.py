class Solution:
    def integerBreak(self, n: int) -> int:
        maxProductMap = {}
        res, coef = 0, 1

        while n >= 10:
            coef *= 3
            n -= 3

        def backtrack(original, remaining, numsUsed):

            if (remaining in maxProductMap or remaining == 0):
                if remaining == 0 and len(numsUsed) == 1:
                    return
                nonlocal res
                x = maxProductMap.get(remaining, 1)

                for num in numsUsed:
                    x *= num
                res = max(res, x)
                maxProductMap[original] = res
                
            for i in range(1, remaining + 1):
                numsUsed.append(i)
                if remaining - i >= 0:
                    backtrack(original, remaining - i, numsUsed)
                    numsUsed.pop()
                else:
                    break

            return res

        for i in range(1, n+1):
            backtrack(i, i, [])

        return coef * res