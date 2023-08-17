# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.bool = True
     
        def traverseTwo(root1, root2):
            if root1 == None or root2 == None:
                if root1 != root2:
                    self.bool = False
                return
                
            if root1.val != root2.val:
                self.bool = False
                return
                
            traverseTwo(root1.left, root2.right)
            traverseTwo(root1.right, root2.left)
            
        traverseTwo(root.left, root.right)
        
        return self.bool