class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict, sDict = {}, {}
        pLength = len(p)

        if pLength > len(s): return []
        
        for i in range(0, pLength):
            if p[i] in pDict: pDict[p[i]] += 1
            else: pDict[p[i]] = 1

            if s[i] in sDict: sDict[s[i]] += 1
            else: sDict[s[i]] = 1

        res = [0] if pDict == sDict else []
        
        i = 1
        j = pLength
        while j < len(s):
            if sDict[s[i-1]] > 1:
                sDict[s[i-1]] -= 1
            else:
                del sDict[s[i-1]]
            
            if s[j] in sDict: sDict[s[j]] += 1
            else: sDict[s[j]] = 1

            if sDict == pDict:
                res.append(i)
                
            i += 1
            j += 1
            
        return res
    
    # What if instead we had a dict initialised with all the letters mapped to occurences of p
    # Each time we loop through the substring we subtract 1 when theres a matching char
    # If all values are 0 when we're finished looping we found a match