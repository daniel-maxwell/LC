class Solution:
    def reverseWords(self, s: str) -> str:
        strArr, wordArr = [], []

        for i in range(len(s)):
            if s[i] == " ":
                strArr.append(''.join(wordArr[::-1]) + " ")
                wordArr = []
            else:
                wordArr.append(s[i])

        return ''.join(strArr) + ''.join(wordArr)[::-1]