class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        a.reverse()
        b.reverse()
        
        i, carry, res = 0, 0, []

        while i < len(a) or i < len(b):
            SUM = 0

            if i < len(a): SUM += int(a[i])
            if i < len(b): SUM += int(b[i])
            if carry:
                SUM += 1
                carry -= 1
            if SUM == 3:
                res.append("1")
                carry += 1
            elif SUM == 2:
                res.append("0")
                carry += 1
            elif SUM == 1:
                res.append("1")
            elif SUM == 0:
                res.append("0")
                
            i += 1

        while carry:
            res.append("1")
            carry -= 1

        res.reverse()
        return ''.join(res)