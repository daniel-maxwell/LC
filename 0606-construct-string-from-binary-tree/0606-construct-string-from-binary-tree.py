# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root: return ""

        def preorder(root):
            if not root: return
            
            res.append(f"({root.val}")
            
            if not root.left and root.right: res.append("()")
            left = preorder(root.left)
            right = preorder(root.right)

            res.append(")")
            return str(root.val) + ")"

        preorder(root)
        return str(root.val) + ''.join(res[1:-1])