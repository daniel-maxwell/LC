class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        i = 0
        while i < len(s):

            if s[i] in mapST and mapST[s[i]] != t[i]:
                return False
            else:
                mapST[s[i]] = t[i]

            
            if t[i] in mapTS and mapTS[t[i]] != s[i]:
                return False

            else:
                mapTS[t[i]] = s[i]

            i += 1

        return True