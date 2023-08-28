class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        starStack = []

        for i in range(len(s) -1, -1, -1):
            if s[i] == '*':
                starStack.append('*')
                s.pop(i)

            else:
                if starStack:
                    s.pop(i)
                    starStack.pop()

        return ''.join(s)