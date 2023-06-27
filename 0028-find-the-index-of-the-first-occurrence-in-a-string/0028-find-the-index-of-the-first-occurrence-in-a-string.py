class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == len(haystack): 
            if needle == haystack: return 0
            else: return -1
        else: 
            for i in range(0, len(haystack) - len(needle)+1):
                substr = haystack[i:i+len(needle)]
                if substr == needle: return i
        return -1