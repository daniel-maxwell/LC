class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        matchingChar = 0
        for char in t:
            if matchingChar < len(s) and s[matchingChar] == char:
                matchingChar+=1
        return matchingChar == len(s)