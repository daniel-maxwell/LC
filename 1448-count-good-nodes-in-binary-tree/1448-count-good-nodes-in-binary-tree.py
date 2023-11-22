# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res, max = 1, root.val

        def dfs(root, max):
            if not root: return 0

            val = 0
            if root.val >= max:
                max = root.val
                val = 1

            lSum = dfs(root.left, max)
            rSum = dfs(root.right, max)
            
            return val + lSum + rSum

        return dfs(root, max)