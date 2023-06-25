class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1

        while (j-i>len(s)%2):
            s[j], s[i] = s[i], s[j]
            i += 1
            j -= 1