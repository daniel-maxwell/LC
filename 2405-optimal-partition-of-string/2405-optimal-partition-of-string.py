class Solution:
    def partitionString(self, s: str) -> int:

        currSet = set()
        sets = 1

        for i in range(0, len(s)):
            if s[i] not in currSet:
                currSet.add(s[i])
            else:
                sets += 1
                currSet = set(s[i])

        return sets       