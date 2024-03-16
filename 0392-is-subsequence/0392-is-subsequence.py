class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        sStack = list(s)

        for i in range(len(t)-1, -1, -1):
            if t[i] == sStack[-1]:
                sStack.pop()

            if not sStack:
                return True

        return False