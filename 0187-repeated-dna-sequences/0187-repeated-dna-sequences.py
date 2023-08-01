class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        oneOccurence, twoOrMore = set(), set()
        window = ""
        l, r = 0, 9
        while r < len(s):
            window = ''.join(s[l:r+1])
            if window in oneOccurence:
                twoOrMore.add(window)
            else:
                oneOccurence.add(window)
            l += 1
            r += 1
        return list(twoOrMore)