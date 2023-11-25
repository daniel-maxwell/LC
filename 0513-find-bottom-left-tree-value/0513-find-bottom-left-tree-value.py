# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        res = q[-1].val

        while q:
            length = len(q)
            i = 0
            res = q[-1].val

            while i < length:
                curr = q.pop()

                if curr.left:
                    q.appendleft(curr.left)

                if curr.right:
                    q.appendleft(curr.right)

                i += 1

        return res