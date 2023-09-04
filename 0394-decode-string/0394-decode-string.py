class Solution:
    def decodeString(self, s: str) -> str:

        nums = set(['0','1','2','3','4','5','6','7','8','9'])
        stack, coef, output, curr = [], '', '', ''

        for i in range(0, len(s)):

            if s[i] == ']':
                while stack[-1] not in nums:
                    if stack[-1] is not '[':
                        curr = stack.pop() + curr
                    else:
                        stack.pop()

                while stack and stack[-1] in nums:
                    coef = stack.pop() + coef

                curr = int(coef) * curr
                stack.append(curr)
                curr, coef = '', ''

            else:
                stack.append(s[i])

        return ''.join(stack)