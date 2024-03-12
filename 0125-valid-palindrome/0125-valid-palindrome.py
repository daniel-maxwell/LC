class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = set(['a', 'b', 'c', 'd', 'e', 
                   'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G',
                   'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'V', 'W', 'X', 'Y', 'Z'])
        
        numbers = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        l, r = 0, len(s) - 1

        while l < r:
            a, b = None, None

            if s[l] in letters:
                a = s[l].lower()
            elif s[l] in numbers:
                a = s[l]
            if s[r] in letters:
                b = s[r].lower()
            elif s[r] in numbers:
                b = s[r]

            if (a and b) or (not (a or b)):
                if a != b:
                    return False
                else:
                    l += 1
                    r -= 1
                    continue

            elif a and not b:
                r -= 1
                continue

            elif b and not a:
                l += 1
                continue

        return True