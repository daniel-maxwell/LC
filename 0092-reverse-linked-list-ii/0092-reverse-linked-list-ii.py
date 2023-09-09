# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right: return head
        stack, counter, l, r = [], 1, head, head

        while r and counter <= right:
            if counter == left: l = r
            if counter >= left: stack.append(r.val)
            counter += 1
            r = r.next    
        
        while counter > left:
            l.val = stack.pop()
            l = l.next
            counter -= 1
      
        return head