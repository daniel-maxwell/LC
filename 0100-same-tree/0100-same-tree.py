# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.bool = True

        def traverseTwo(root1, root2):
            if root1 and root2:
                if root1.val != root2.val:
                    self.bool = False
                    return
                traverseTwo(root1.left, root2.left)
                traverseTwo(root1.right, root2.right)
            elif root1 or root2:
                self.bool = False
                return

        traverseTwo(p, q)
        return self.bool