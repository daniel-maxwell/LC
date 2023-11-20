# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q, height = deque([root]), 0

        while q:
            nodeCount, i, length = 0, 0, len(q)
            filled = True

            while i < length:
                curr = q.pop()

                if curr.left:
                    if not filled: return False
                    q.appendleft(curr.left)
                    nodeCount += 1
                else:
                    filled = False

                if curr.right:
                    if not filled: return False
                    q.appendleft(curr.right)
                    nodeCount += 1

                else: 
                    filled = False

                i += 1
            height += 1
            
            if len(q) < 2 ** height: break

        for i in range(0, len(q)):
            if q[i].left or q[i].right: return False

        return True