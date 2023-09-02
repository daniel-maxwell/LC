class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        charStack = []
        occStack = []

        for i in range(0, len(s)):

            if charStack and charStack[-1] == s[i]:

                if occStack[-1] == k-1:  # enough occurences to pop

                    while occStack[-1] > 0:
                        charStack.pop()
                        occStack[-1] -= 1

                    occStack.pop()

                else:
                    charStack.append(s[i])
                    occStack[-1] += 1

            else:
                charStack.append(s[i])
                occStack.append(1)

        return "".join(charStack)