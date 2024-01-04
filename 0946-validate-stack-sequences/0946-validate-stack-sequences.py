class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed[0]]
        i, j = 1, 0

        while i < len(pushed) and j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                stack.append(pushed[i])
                i += 1

        while stack:
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False

        return True