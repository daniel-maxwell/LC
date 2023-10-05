'''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def cloneAndTraverse(node):
            if node in oldToNew:    # We already made a clone of this node.
                return oldToNew[node]   # so just return it

            # otherwise...

            clone = Node(node.val)   # construct a new clone node w/ the val of the original node

            oldToNew[node] = clone   # map the original node to the clone in our hash map

            # recursively make copies of every neighbor of the current node and append the copies to the list of neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(cloneAndTraverse(neighbor))

            # once we're done copying the neighbors, return the copy of the node we just created (with all its neighbors)
            return clone

        return cloneAndTraverse(node) if node else None     # covers edge case of node being null value