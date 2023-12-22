class Solution:
    def bestClosingTime(self, customers: str) -> int:
        profit, p, l = [0], 0, 0

        for i in range(0, len(customers)):
            if customers[i] == "Y":
                p += 1      
            profit.append(p)
        
        for i in range(0, len(customers)):
            if customers[i] == "N":
                l += 1
            profit[i+1] -= l

        maximum = float('-inf')
        res = -1
        for i in range(0, len(profit)):
            if profit[i] > maximum:
                maximum = profit[i]
                res = i

        return res