# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        currStr, total = "", 0

        def dfs(root):
            nonlocal currStr
            nonlocal total
            
            if not root: return

            currStr += str(root.val)

            if not (root.left or root.right):
                total += int(currStr)

            dfs(root.left)
            dfs(root.right)
            currStr = currStr[:-1]

        dfs(root)

        return total