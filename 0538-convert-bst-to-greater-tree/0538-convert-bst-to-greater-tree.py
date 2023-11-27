# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currSum = 0

        def reverseInorder(root):
            if not root: return
            
            nonlocal currSum
            
            reverseInorder(root.right)
            
            currSum += root.val
            root.val = currSum
            
            reverseInorder(root.left)

        reverseInorder(root)
        return root