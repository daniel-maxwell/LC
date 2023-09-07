# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        stop = stack[len(stack)//2]

        while curr is not stop:
            Next = curr.next
            curr.next = stack.pop()
            curr = curr.next
            curr.next = Next
            curr = curr.next

        curr.next = None