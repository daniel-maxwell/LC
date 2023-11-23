# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validLeft(root, val):
            if not root:
                return True
            res = False if root.val >= val else True
            if not res: return False
            return res and validLeft(root.left, val) and validLeft(root.right, val)

        def validRight(root, val):
            if not root:
                return True
            res = False if root.val <= val else True
            if not res: return False
            return res and validRight(root.left, val) and validRight(root.right, val)

        def dfs(root):
            if not root: return True
            res = True
            if not validLeft(root.left, root.val): res = False
            if not validRight(root.right, root.val): res = False

            return res and dfs(root.left) and dfs(root.right)

        return dfs(root)