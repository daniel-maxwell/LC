class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l, r = 0, len(word) - 1
            pal = True
            while l <= r:
                if word[l] != word[r]:
                    pal = False
                    break
                l += 1
                r -= 1
                
            if pal:
                return word

        return ""