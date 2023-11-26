# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return
            
            while node.left and node.left.val < low:
                if node.left.right and node.left.right.val <= high:
                    node.left = node.left.right
                else:
                    node.left = None

            while node.right and node.right.val > high:
                if node.right.left and node.right.left.val >= low:
                    node.right = node.right.left
                else:
                    node.right = None

            dfs(node.left)
            dfs(node.right)

        while not (low <= root.val <= high):
            if root.val < low:
                if not root.right: return None
                root = root.right

            elif root.val > high:
                if not root.left: return None
                root = root.left

        dfs(root)
        return root