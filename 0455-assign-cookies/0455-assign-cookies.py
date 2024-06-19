class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        numChildren = 0
        i = len(s) - 1

        while i >= 0:
            if not g:
                break
            if s[i] >= g[-1]:
                numChildren += 1
                i -= 1
            g.pop()

        return numChildren