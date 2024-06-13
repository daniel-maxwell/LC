class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(t)

        for char in s:
            c[char] -= 1
            if c[char] == 0:
                c.pop(char)

        return c.popitem()[0]  