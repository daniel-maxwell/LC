class Solution:
    def partitionString(self, s: str) -> int:
        charSet, result = set(), 1

        for char in s:
            if char in charSet:
                result += 1
                charSet = set()
            charSet.add(char)

        return result
