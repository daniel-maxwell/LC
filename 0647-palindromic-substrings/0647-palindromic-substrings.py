class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)

        for i in range(0, len(s)):
            
            # odd length
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

        return res