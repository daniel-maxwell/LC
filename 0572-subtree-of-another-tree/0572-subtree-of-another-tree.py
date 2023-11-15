# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = [False]
        def sameTree(r1, r2):
            if not r1 and not r2:
                return True

            if not (r1 and r2):
                return False

            return ((r1.val == r2.val) and 
            (sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)))


        def preOrder(root):
            if not root:
                return

            if sameTree(root, subRoot):
                res[0] = True
            preOrder(root.left)
            preOrder(root.right)

        
        preOrder(root)

        return res[0]