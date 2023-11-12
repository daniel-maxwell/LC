# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Recursively traverse all the way down to the leaves.
        # At the leaves, the subtrees are inherently balanced.
        # Simply pass back up the heights of the subtrees starting from 
        # each node to the preceding recurive call
        # using the heights of the subtrees, it's easy to compare them
        # to determine if the subtrees are indeed balanced
        # Do this until the call stack returns to the root node
        # If the balanced boolean is still true and the heights are
        # <= 1, then we know the tree is balanced


        balanced = True
        def dfs(root):
            if not root: return [True, 0]

            # Recursively traverses to the leaves
            l, r = dfs(root.left), dfs(root.right)

            # Only true if after calculating heights of subtrees,
            # We determine they are balanced AND at no other point
            # did we find an unbalanced subtree
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1


            # index 0: the balanced boolean
            # index 1: the height of the subtree, (in other words
            # the maximum depth of the subtree.) We add 1 to
            # account for the current node
            return [balanced, 1 + max(l[1], r[1])]

        return dfs(root)[0]