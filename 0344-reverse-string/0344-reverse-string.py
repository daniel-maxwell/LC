class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1

        while (j-i>len(s)%2):
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i += 1
            j -= 1