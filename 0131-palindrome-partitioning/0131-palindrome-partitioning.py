class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def allPalindromes(strList):
            for s in strList:
                i, j = 0, len(s) - 1
                while i <= j:
                    if s[i] != s[j]: return False
                    i += 1
                    j -= 1
            return True

        res = []
        if allPalindromes([s]): res.append([s])

        def backtrack(curr, l, r, pCount):
            if r == len(s): return

            curr.append(s[l:r])
            
            if pCount == 1:
                curr.append(s[r:])
                if allPalindromes(curr):
                    res.append(curr.copy())
                curr.pop()
                curr.pop()
                backtrack(curr, l, r+1, pCount)
                return

            else:
                backtrack(curr, r, r+1, pCount - 1)
                curr.pop()
                backtrack(curr, l, r+1, pCount)
            
            return

        for i in range(1, len(s)):
            backtrack([], 0, 1, i)

        return res