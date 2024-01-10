# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        nodes = []
        curr = head

        while curr:
            temp = curr.next
            curr.next = None
            nodes.append(curr)
            curr = temp

        for n in range(0, len(nodes)-1, 2):
            nodes[n], nodes[n+1] = nodes[n+1], nodes[n]

        head = nodes[0]

        for n in range(0, len(nodes)-1):
            nodes[n].next = nodes[n+1]

        return head