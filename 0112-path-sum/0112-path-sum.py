# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target = targetSum
        self.outcome = False

        def traverse(root):

            if root:

                if not root.left and not root.right:
                    # it's a leaf
                    if self.target - root.val == 0:
                        self.outcome = True
                    return

                else:
                    self.target -= root.val
                    traverse(root.left)
                    traverse(root.right)
                    self.target += root.val
                    return
            else:
                return

        traverse(root)

        return self.outcome

        