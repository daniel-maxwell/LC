class Solution:
    def partitionString(self, s: str) -> int:
        charSet = set()
        result = 1

        for i in range(len(s)):
            if s[i] in charSet:
                result += 1
                charSet = set()
            charSet.add(s[i])

        return result