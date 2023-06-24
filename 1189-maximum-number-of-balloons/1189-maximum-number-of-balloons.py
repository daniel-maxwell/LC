class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCounts = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        for i in range(0, len(text)):
            if text[i] in charCounts:
                charCounts[text[i]] += 1
        charCounts['l'] = math.floor(charCounts['l']/2)
        charCounts['o'] = math.floor(charCounts['o']/2)
        return min(charCounts.values())