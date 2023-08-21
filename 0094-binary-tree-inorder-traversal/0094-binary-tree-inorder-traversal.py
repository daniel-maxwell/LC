# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def inorder(rootNode):
            if not rootNode:
                return

            inorder(rootNode.left)
            output.append(rootNode.val)
            inorder(rootNode.right)

        inorder(root)
        return output