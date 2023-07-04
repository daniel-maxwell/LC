class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        length = len(word1) if len(word1) <= len(word2) else len(word2)

        for i in range(0, length+1):
            if i == len(word1) and i == len(word2):
                return output
            elif i == len(word1):
                return output + word2[i:]
            elif i == len(word2):
                return output + word1[i:]
            output += word1[i]
            output += word2[i]