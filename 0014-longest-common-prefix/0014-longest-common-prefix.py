class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char = ''
        i = 0
        for i in range(0, len(strs[0])):
            for j in range(0, len(strs)): 
                if j == 0: char = strs[j][i]
                else: 
                    if i > (len(strs[j]) -1) or char != strs[j][i]: return strs[0][0:i]
            i+=1
        return strs[0][0:i]