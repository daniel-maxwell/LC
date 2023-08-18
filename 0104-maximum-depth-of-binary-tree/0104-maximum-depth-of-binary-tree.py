# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxcount = 0
        self.currcount = 0

        if not root:
            return 0

        def preorder(root):      
            if not root:
                if self.currcount > self.maxcount:
                    self.maxcount = self.currcount
                return
            else:
                self.currcount += 1
                
            preorder(root.left)
            preorder(root.right)
            self.currcount -= 1

        preorder(root)
        return self.maxcount