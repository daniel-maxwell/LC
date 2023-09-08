# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack, curr = [], head

        while curr:
            stack.append(curr)
            curr = curr.next

        if len(stack) == 1:
            return None

        if n == 1:
            stack.pop()
            stack[-1].next = None
            return head

        if n == len(stack):
            stack[0].next = None
            head = stack[1]
            return head

        while n > 2:
            stack.pop()
            n -= 1

        Next = stack.pop()
        stack.pop()
        stack[-1].next = Next
        return head