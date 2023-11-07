class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        x = str(x)
        if len(x) == 1: return True

        i = 0
        j = len(x) - 1

        while i < j:

            if x[i] != x[j]:
                return False

            i += 1
            j -= 1

        return True