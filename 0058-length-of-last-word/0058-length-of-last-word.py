class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip().split(" ")
        return len(s[len(s)-1])
        