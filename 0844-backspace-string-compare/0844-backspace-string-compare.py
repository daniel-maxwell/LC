class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        backspaces = 0
        sArr, tArr = [], []
        for i in range(len(s)-1, -1, -1):
            if s[i] == "#":
                backspaces += 1
            else:
                if backspaces > 0:
                    backspaces -= 1
                else:
                    sArr.append(s[i])

        backspaces = 0
        for i in range(len(t)-1, -1, -1):
            if t[i] == "#":
                backspaces += 1
            else:
                if backspaces > 0:
                    backspaces -= 1
                else:
                    tArr.append(t[i])

        return sArr == tArr