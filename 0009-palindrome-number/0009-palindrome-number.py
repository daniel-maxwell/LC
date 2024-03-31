class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = list(str(x))
        b.reverse()
        return str(x) == ''.join(b)
        