# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        res, q = [], deque([root])

        while q:
            count, length, last = 0, len(q), None

            while count < length:
                curr = q.pop()
                last = curr.val
                if curr.left: q.appendleft(curr.left)
                if curr.right: q.appendleft(curr.right)
                count += 1
            res.append(last)

        return res