# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root, pathSum):
            if not root:
                return False
            if not (root.left or root.right):
                if pathSum + root.val == targetSum:
                    return True
                return False

            pathSum += root.val
            result = dfs(root.left, pathSum) or dfs(root.right, pathSum)
            pathSum -= root.val

            return result

        return dfs(root, 0)