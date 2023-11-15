# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def isParent(node, potentialChild):
            res = [False]

            def traverse(root):
                if not root:
                    return False
                if res[0]: return
                if root.val == potentialChild.val:
                    res[0] = True
                traverse(root.left)
                traverse(root.right)

            traverse(node)
            return res[0]

        lowest = [root]

        def findLCA(root, p, q):
            if not root:
                return

            if (isParent(root, p) and isParent(root, q)):
                lowest[0] = root

            findLCA(root.left, p, q)
            findLCA(root.right, p, q)

        findLCA(root, p, q)

        return lowest[0]