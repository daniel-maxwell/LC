# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 and root2:
            root1.val += root2.val
        else:
            return root1 if root1 else root2

        def dfs(r1, r2):

            if r1.left and r2.left:
                r1.left.val += r2.left.val
                dfs(r1.left, r2.left)

            elif not r1.left and r2.left:
                r1.left = r2.left
            

            if r1.right and r2.right:
                r1.right.val += r2.right.val
                dfs(r1.right, r2.right)

            elif not r1.right and r2.right:
                r1.right = r2.right

        dfs(root1, root2)

        return root1