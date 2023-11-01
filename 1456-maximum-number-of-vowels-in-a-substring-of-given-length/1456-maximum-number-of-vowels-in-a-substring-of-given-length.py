class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])

        maxVowels = 0

        for char in s[0:k]:
            if char in vowels:
                maxVowels += 1

        l, r, currVowels = 0, k, maxVowels

        while r < len(s):
            if s[l] in vowels:
                currVowels -= 1

            l += 1

            if s[r] in vowels:
                currVowels += 1

            r += 1

            maxVowels = max(currVowels, maxVowels)

        return maxVowels 