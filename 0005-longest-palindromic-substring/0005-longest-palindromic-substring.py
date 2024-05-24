class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(len(s)):

            # odd length palindromes
            l, r = i, i + 1
            length = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                l -= 1
                r += 1

            result = s[l + 1 : r] if length > len(result) else result

            # even length palindromes
            l, r = i - 1, i + 1
            length = 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                l -= 1
                r += 1

            result = s[l + 1 : r] if length > len(result) else result

        return result