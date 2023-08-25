# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not (root1 and root2):
            return root1 if root1 else root2

        def traverseAndMerge(root1, root2):

            if not (root1 or root2):
                return

            if not (root1 and root2):
                return root1 if root1 else root2

            curr = TreeNode(root1.val + root2.val)
  
            curr.left = traverseAndMerge(root1.left, root2.left)
            curr.right = traverseAndMerge(root1.right, root2.right)

            return curr

        root = traverseAndMerge(root1, root2)

        return root