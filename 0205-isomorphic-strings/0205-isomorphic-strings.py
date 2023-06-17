class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        u = []
        v = []
        for i in range(0, len(s)):
            if s[i] in dict_s:
                u.append(dict_s[s[i]])
            else: 
                dict_s[s[i]] = i
                u.append(i)
            if t[i] in dict_t:
                v.append(dict_t[t[i]])
            else: 
                dict_t[t[i]] = i
                v.append(i)
        return u == v