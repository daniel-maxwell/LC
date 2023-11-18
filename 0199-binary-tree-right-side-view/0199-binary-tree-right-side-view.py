# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        res = []
        q = deque([root])

        while q:

            level = []
            length = len(q)

            while len(level) < length:

                curr = q.pop()
                level.append(curr.val)

                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)

            res.append(level[-1])

        return res