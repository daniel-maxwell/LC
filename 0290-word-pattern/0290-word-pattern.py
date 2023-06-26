class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s): return False
        mapPS = {}
        mapSP = {}

        for i in range(0, len(s)):
            if pattern[i] in mapPS and mapPS[pattern[i]] != s[i]:
                return False
            else: mapPS[pattern[i]] = s[i]
            
            if s[i] in mapSP and mapSP[s[i]] != pattern[i]:
                return False
            else: mapSP[s[i]] = pattern[i]

        return True