# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap, res = [], None

        def dfs(root):
            if not root: return

            heapq.heappush(heap, root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        while k:
            res = heapq.heappop(heap)
            k -= 1

        return res