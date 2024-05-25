class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(0, len(s)):

            # odd length

            found = 1
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                found += 1
                l -= 1
                r += 1

            res += found

            # even length
            found = 0
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                found += 1
                l -= 1
                r += 1

            res += found

        return res