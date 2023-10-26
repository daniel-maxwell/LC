class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0: return 0
        elif len(s) == 1: return 1

        maxLength, currLength = 1, 1
        charSet = set([s[0]])
        i, j = 0, 1

        while j < len(s):

            if s[j] not in charSet:
                currLength += 1
                charSet.add(s[j])

            else:
                if s[i] == s[j]:
                    i += 1
                else:
                    while s[i] != s[j]:
                        charSet.remove(s[i])
                        i += 1
                    i += 1
                    currLength = (j - i) + 1

            if currLength > maxLength: maxLength = currLength

            j += 1

        return max(maxLength, len(charSet))