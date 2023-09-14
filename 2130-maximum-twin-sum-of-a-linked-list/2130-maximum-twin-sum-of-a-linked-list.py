# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack, curr = [], head

        while curr:
            stack.append(curr)
            curr = curr.next
        
        counter, max, curr, n = 0, 0, head, len(stack)

        while counter < n // 2:
            twinSum = curr.val + stack.pop().val
            if twinSum > max:
                max = twinSum
            curr = curr.next
            counter += 1

        return max