class Solution:
    def removeStars(self, s: str) -> str:
        starStack = []

        for i in range(len(s) -1, -1, -1):
            if s[i] == '*':
                starStack.append('*')
                s = s[:i] + s[i + 1:]

            else:
                if starStack:
                    s = s[:i] + s[i + 1:]
                    starStack.pop()

        return s