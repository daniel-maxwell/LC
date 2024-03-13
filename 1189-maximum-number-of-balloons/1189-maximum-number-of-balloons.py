class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        charCount = {
            "b": 0,
            "a": 0,
            "l": 0,
            "l": 0,
            "o": 0,
            "o": 0,
            "n": 0,
        }

        for char in text:
            if char in charCount:
                charCount[char] += 1
                
        charCount["l"] = charCount["l"] // 2
        charCount["o"] = charCount["o"] // 2

        return min(charCount.values())