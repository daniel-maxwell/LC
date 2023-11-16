# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        result = []
        queue = deque([root])

        while queue:
            level = []
            sz = len(queue)
            while sz > 0:
                curr = queue.pop() 
                level.append(curr.val)
                if curr.left: queue.appendleft(curr.left)
                if curr.right: queue.appendleft(curr.right)
                sz -= 1

            result.append(level)
            
        return result