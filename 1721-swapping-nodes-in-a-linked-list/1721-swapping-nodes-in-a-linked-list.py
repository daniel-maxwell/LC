# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack, curr, count, first = [], head, k, None

        while curr:
            stack.append(curr)
            count -= 1
            if count == 0:
                first = curr
            curr = curr.next

        while k > 1:
            stack.pop()
            k -= 1
    
        first.val, stack[-1].val = stack[-1].val, first.val

        return head