class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        numeralMap = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1
        }
        i = len(s) - 1
        prevNum = 0

        while i >= 0:
            currNum = numeralMap[s[i]]
            if currNum < prevNum:
                output -= currNum
            else:
                output += currNum
            prevNum = currNum
            i -= 1
        
        return output