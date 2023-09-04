class Solution:
    def decodeString(self, s: str) -> str:
        stack, coef, output, curr = [], '', '', ''

        for i in range(0, len(s)):

            if s[i] == ']':
                while not stack[-1].isdigit():
                    if stack[-1] is not '[':
                        curr = stack.pop() + curr
                    else:
                        stack.pop()

                while stack and stack[-1].isdigit():
                    coef = stack.pop() + coef

                curr = int(coef) * curr
                stack.append(curr)
                curr, coef = '', ''

            else:
                stack.append(s[i])

        return ''.join(stack)