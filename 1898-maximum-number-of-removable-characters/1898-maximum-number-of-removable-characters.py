class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(s, p):
            l = 0
            for char in s:
                if l == len(p):
                    return True
                if char == p[l]:
                    l += 1
            return l >= len(p)

        l, r, res = 0, len(removable) - 1, 0
        m = l + ((r-l) // 2)
        currS, prevM = s, m
        i = 0

        while i <= m:
            currS = currS[:removable[i]] + "0" + currS[removable[i]+1:]
            i += 1

        while l <= r:

            if isSubsequence(currS, p):
                if m + 1 > res: res = m + 1
                l = m + 1
            else:
                r = m - 1

            prevM = m
            m = l + ((r-l) // 2)

            if m < prevM:
                start = prevM
                stop = m
                for i in range(m+1, prevM+1):
                    currS = currS[:removable[i]] + s[removable[i]] + currS[removable[i]+1:]

            else:
                start = prevM + 1
                stop = m
                for i in range(start, stop+1):
                    currS = currS[:removable[i]] + "0" + currS[removable[i]+1:]

        return res