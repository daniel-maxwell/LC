class Solution:
    def maxLength(self, arr: List[str]) -> int:

        charSetMap = {}

        for i, val in enumerate(arr):
            SET = set(val)
            if len(SET) != len(val):
                charSetMap[i] = set()
            else:
                charSetMap[i] = SET

        maxL = len(charSetMap[0])

        def backtrack(curr, currL, maxL, i):
            if i == len(arr):
                return maxL

            if not curr.intersection(charSetMap[i]):
                currL += len(charSetMap[i])
                newCurr = curr.copy()
                newCurr.update(charSetMap[i])
                maxL = max([maxL, currL, backtrack(newCurr, currL, maxL, i + 1)])
                currL -= len(charSetMap[i])

            maxL = max([currL, maxL, backtrack(curr, currL, maxL, i + 1)])

            return maxL

        return backtrack(set(), 0, maxL, 0)