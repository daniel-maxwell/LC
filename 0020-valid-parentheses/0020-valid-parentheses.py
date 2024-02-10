class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        for char in s:
            if char in bracketMap:
                stack.append(bracketMap[char])
            else:
                if not stack or stack[-1] != char:
                    return False
                stack.pop()
                
        return True if not stack else False