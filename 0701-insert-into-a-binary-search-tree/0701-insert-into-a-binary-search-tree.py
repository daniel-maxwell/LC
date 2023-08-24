# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            if self.prev:
                if self.prev.val > root.val:
                    self.prev.left = root
                else:
                    self.prev.right = root     

        else:
            self.prev = root
            if val < root.val:
                self.insertIntoBST(root.left, val)

            else:
                self.insertIntoBST(root.right, val)
        
        return root