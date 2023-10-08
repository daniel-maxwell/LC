class Solution:
    def isHappy(self, n: int) -> bool:
        nSet = set()
        
        while n > 1 and n not in nSet:
            nSet.add(n)
            sum = 0
            k = str(n)

            for i in range(0, len(k)):
                sum += int(k[i]) ** 2
            n = sum
            
        return n == 1 