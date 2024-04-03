# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head: return head
        length, curr = 0, head

        while curr:
            curr = curr.next
            length += 1

        offset = k % length

        if offset == 0:
            return head

        dummy = ListNode(0, head)
        index, curr = 0, head
    
        while index < length - offset - 1:
            curr = curr.next
            index += 1

        dummy.next = curr.next
        curr.next = None
        curr = dummy.next

        while curr.next:
            curr = curr.next

        curr.next = head

        return dummy.next