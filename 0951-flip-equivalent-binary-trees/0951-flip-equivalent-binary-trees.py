# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(r1, r2):
            if (r1 and not r2) or (r2 and not r1): return False
            if not (r1 or r2): return True
            if r1.val != r2.val: return False
            
            r1Left = r1.left.val if r1.left else None
            r1Right = r1.right.val if r1.right else None
            r2Left = r2.left.val if r2.left else None
            r2Right = r2.right.val if r2.right else None

            if (r1Left, r1Right) != (r2Left, r2Right):

                if (r1Left, r1Right) != (r2Right, r2Left):
                    return False
                else:
                    r2.left, r2.right = r2.right, r2.left

            return True and dfs(r1.left, r2.left) and dfs(r1.right, r2.right)

        return dfs(root1, root2)