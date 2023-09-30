class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1: return False
        uglySet = set([2, 3, 5])

        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                print(i)
                if i not in uglySet:
                    return False
        if n > 1:
            if n not in uglySet:
                return False

        return True