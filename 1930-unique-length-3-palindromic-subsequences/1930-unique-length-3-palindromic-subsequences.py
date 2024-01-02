class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        def indexNoExcept(self, char, lst, start=0):
            for i in range(start, len(lst)):
                if lst[i] == char:
                    return i
            return None
            
        found, s, result = set(), deque(list(s)), 0

        while len(s) > 2:
            first = s.popleft()
            lastIdx = indexNoExcept(self, first, s)
            if lastIdx == None: continue

            for i in range(0, lastIdx):
                pal = first + s[i] + s[lastIdx]
                if pal not in found:
                    found.add(pal)
                    result += 1

            if first + first + first not in found:
                if indexNoExcept(self, first, s, lastIdx+1):
                    found.add(first + first + first)
                    result += 1

        return result