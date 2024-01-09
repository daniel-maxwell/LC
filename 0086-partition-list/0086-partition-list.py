# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l, r = [], []
        curr = head

        while curr:
            if curr.val < x:
                l.append(curr.val)
            else:
                r.append(curr.val)
            curr = curr.next

        l.extend(r)
        i = 0
        curr = head
        while curr:
            curr.val = l[i]
            i += 1
            curr = curr.next
        return head