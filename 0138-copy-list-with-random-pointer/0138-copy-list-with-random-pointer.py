"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToIdx, nodes = {}, []

        curr, counter = head, 0

        while curr:
            nodeToIdx[curr] = counter
            nodes.append(Node(curr.val))
            curr = curr.next
            counter += 1

        for i in range(0, len(nodes)-1):
            nodes[i].next = nodes[i+1]
        
        i = 0
        curr = head
        while curr:
            if curr.random in nodeToIdx:
                nodes[i].random = nodes[nodeToIdx[curr.random]]
            curr = curr.next
            i += 1

        return nodes[0] if nodes else None