# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack, vals, curr = [], [], head

        while curr:
            stack.append(curr)
            vals.append(curr.val)
            curr = curr.next

        vals.sort()

        while stack:
            stack.pop().val = vals.pop()

        return head