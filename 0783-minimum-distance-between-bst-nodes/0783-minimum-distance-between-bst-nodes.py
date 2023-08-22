

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        self.set = []

        def preorder(root):
            if root == None:
                return
            self.set.append(root.val)
            preorder(root.left)
            preorder(root.right)


        preorder(root.left)
        self.set.append(root.val)
        preorder(root.right)

        def findMinDiff(arr):
            n = len(arr)
            # Initialize difference as infinite
            diff = 10**20
        
            # Find the min diff by comparing difference
            # of all possible pairs in given array
            for i in range(n-1):
                for j in range(i+1, n):
                    if abs(arr[i]-arr[j]) < diff:
                        diff = abs(arr[i] - arr[j])
        
            # Return min diff
            return diff
        
        return findMinDiff(self.set)