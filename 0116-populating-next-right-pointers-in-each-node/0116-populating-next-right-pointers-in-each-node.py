"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        levels = {}

        def dfs(root, lvlcount):
            if not root:
                return

            if lvlcount in levels:
                levels[lvlcount].append(root)
            else:
                levels[lvlcount] = [root]

            lvlcount += 1

            dfs(root.left, lvlcount)
            dfs(root.right, lvlcount)

        dfs(root, 1)

        for level in levels.values():
            for i in range(len(level)):
                if i + 1 == len(level):
                    level[i].next = None
                else:
                    level[i].next = level[i+1]

        return root