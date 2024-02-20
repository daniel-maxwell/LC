# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        l, r = head, head.next

        if not r:
            return head
        else:
            head.next = None

        while r:
            tmp = r.next
            r.next = l
            l = r
            r = tmp

        return l