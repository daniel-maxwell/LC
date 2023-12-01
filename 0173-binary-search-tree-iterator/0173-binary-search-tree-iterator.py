# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        def dfs(root):
            if not root: return
            dfs(root.right)
            self.stack.append(root)
            dfs(root.left)

        dfs(root)
        self.pointer = -1
        
    def next(self) -> int:
        self.pointer = self.stack.pop().val
        return self.pointer
        
    def hasNext(self) -> bool:
        if self.stack: return True
        else: return False
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()