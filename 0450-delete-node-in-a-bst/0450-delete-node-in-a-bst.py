# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev, curr = None, root
        if root == None: return None

        if root.val == key: # iterate through until you find leaf node, and replace
            subCurr = None

            if root.left:
                subCurr = root.left

                while subCurr.right != None:
                    prev, subCurr = subCurr, subCurr.right 
                root.val = subCurr.val # make the swap   

                if prev:
                    if subCurr.left: prev.right = subCurr.left
                    else: prev.right = None
                else:
                    if subCurr.left: root.left = subCurr.left
                    else: root.left = None
                return root

            elif curr.right:
                subCurr = root.right

                while subCurr.left != None:
                    prev, subCurr = subCurr, subCurr.left
                root.val = subCurr.val # make the swap
            
                if prev:
                    if subCurr.right: prev.left = subCurr.right
                    else: prev.left = None
                else:
                    if subCurr.right: root.right = subCurr.right
                    else: root.right = None

                return root

            else: return None


        while curr and curr.val != key:  # search
            prev = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if curr == None: return root
        if prev == None:
            if not (curr.left or curr.right): return prev

        if curr.left is None and curr.right is None:  # case 1
            if prev.left and prev.left == curr: prev.left = None
            else: prev.right = None      
            return root
         
        elif (curr.left and not curr.right) or (curr.right and not curr.left):  # case 2
            if curr.left:
                if prev.left and prev.left == curr: prev.left = curr.left
                else: prev.right = curr.left
            else:
                if prev.left and prev.left == curr: prev.left = curr.right
                else: prev.right = curr.right          
            return root
 

        subCurr, prev = curr.right, None   # case 3
        
        while subCurr.left != None:
            prev, subCurr = subCurr, subCurr.left 
        curr.val = subCurr.val
        
        if prev:
            if subCurr.right: prev.left = subCurr.right
            else: prev.left = None
        else:
            if subCurr.right:
                curr.right = subCurr.right
            else: curr.right = None

        return root