# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        reverse = False
        queue = deque([root])
        result = []

        while queue:
            length = len(queue)
            level = []

            while len(level) < length:

                if reverse:
                    curr = queue.popleft()
                    level.append(curr.val)
                    if curr.right: queue.append(curr.right)
                    if curr.left: queue.append(curr.left)
                else:
                    curr = queue.pop()
                    level.append(curr.val)
                    if curr.left: queue.appendleft(curr.left)
                    if curr.right: queue.appendleft(curr.right)

            reverse = not reverse
            result.append(level)

        return result