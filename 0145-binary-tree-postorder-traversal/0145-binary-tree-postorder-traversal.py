# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def postorder(rootNode):
            if not rootNode:
                return
            postorder(rootNode.left)
            postorder(rootNode.right)
            output.append(rootNode.val)

        postorder(root)
        return output