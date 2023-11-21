# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        q = deque([[root, 1, 0]]) # TreeNode(), Assigned number, Level
        prevLvl, firstNodeNum = 0, 1

        while q:
            node, assignedNum, lvl = q.popleft()    # destructure curr node

            if lvl > prevLvl:       # Update previous level and assigned number
                prevLvl = lvl
                firstNodeNum = assignedNum

            res = max(res, assignedNum - firstNodeNum + 1) # update max width if necessarry

            if node.left:
                q.append([node.left, 2 * assignedNum, lvl + 1])

            if node.right:
                q.append([node.right, 2 * assignedNum + 1, lvl + 1])

        return res