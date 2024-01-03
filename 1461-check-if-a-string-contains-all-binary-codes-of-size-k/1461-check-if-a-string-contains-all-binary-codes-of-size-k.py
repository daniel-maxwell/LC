class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        
        l, r = 0, k
        while r <= len(s):
            codes.add(s[l:r])
            l += 1
            r += 1

        return len(codes) == 2**k