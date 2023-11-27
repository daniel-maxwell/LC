# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = [0]

        def reverseInorder(root):
            if not root: return

            reverseInorder(root.right)
            sums[0] += root.val
            root.val = sums[0]
            reverseInorder(root.left)

        reverseInorder(root)

        return root