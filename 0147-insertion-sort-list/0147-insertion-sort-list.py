# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def popFromLL(prev, curr, nxt):
            prev.next = nxt
            curr.next = None
            return curr

        def insertIntoLL(prev, node, nxt):
            prev.next = node
            node.next = nxt

        dummy = ListNode(-5001, head)
        prev, curr = dummy, head

        while curr:
            if curr.val < prev.val:
                node = popFromLL(prev, curr, curr.next)
                pointer = dummy
                while node.val > pointer.next.val:
                    pointer = pointer.next
                insertIntoLL(pointer, node, pointer.next)
                head = dummy.next
            prev = curr
            curr = curr.next
        return head