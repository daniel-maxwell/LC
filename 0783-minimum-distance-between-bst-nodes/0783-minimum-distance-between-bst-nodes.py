# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []

        def dfs(root):
            if not root:
                return

            nodes.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        nodes.sort()

        minDiff = nodes[1] - nodes[0]

        i, j = 1, 2

        while j < len(nodes):
            minDiff = min(minDiff, nodes[j] - nodes[i])
            i += 1
            j += 1

        return minDiff