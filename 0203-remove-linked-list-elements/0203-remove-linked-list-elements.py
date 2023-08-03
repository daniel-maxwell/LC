# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            if curr == head and curr.val == val:
                head = head.next

            elif curr.next == None and curr.val == val:
                prev.next = None

            elif curr.val == val:
                prev.next = curr.next
                curr = prev
            
            prev = curr
            curr = curr.next

        return head