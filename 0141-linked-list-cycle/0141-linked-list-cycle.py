# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        a, b = head, head.next

        while a != b:
            a = a.next
            
            if not b:
                return False
            b = b.next
            if not b:
                return False

            b = b.next

        return True