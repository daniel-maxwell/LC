class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        maxLength, currLength = 1, 1
        l, r = 0, 1
        charSet = set(s[l])
        
        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                currLength += 1
                r += 1

            elif r - l > 1:
                charSet.remove(s[l])
                currLength -= 1
                l += 1

            else:
                l = r
                r += 1
            
            maxLength = max(currLength, maxLength)
        
        return maxLength