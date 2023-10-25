class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(removeIndices): 
            i, j = 0, 0
            while i < len(p) and j < len(s): 
                if j in removeIndices: 
                    j += 1
                elif p[i] == s[j]: 
                    i += 1
                    j += 1
                else: 
                    j += 1
            return i == len(p)
        
        l, r = 0, len(removable)
        maxK = 0
        while l <= r: 
            k = (l + r) // 2
            removeIndices = set(removable[:k])
            if isSubsequence(removeIndices): 
                maxK = max(maxK, k)
                l = k + 1
            else: 
                r = k - 1
        return maxK