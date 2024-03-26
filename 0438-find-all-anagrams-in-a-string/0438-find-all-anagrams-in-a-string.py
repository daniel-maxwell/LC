class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        pCharCounts, sCharCounts = {}, {}

        for char in p:
            if char in pCharCounts:
                pCharCounts[char] += 1
            else:
                pCharCounts[char] = 1

        for i in range(len(p)):
            if s[i] in sCharCounts:
                sCharCounts[s[i]] += 1
            else:
                sCharCounts[s[i]] = 1

        l, r, res = 0, len(p), []

        while r < len(s):
            
            if sCharCounts == pCharCounts:
                res.append(l)
            
            sCharCounts[s[l]] -= 1
            if sCharCounts[s[l]] == 0:
                sCharCounts.pop(s[l])

            if s[r] in sCharCounts:
                sCharCounts[s[r]] += 1
            else:
                sCharCounts[s[r]] = 1

            l += 1
            r += 1

        if sCharCounts == pCharCounts:
            res.append(l)

        return res