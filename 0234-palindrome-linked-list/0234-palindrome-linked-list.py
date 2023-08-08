# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:         
        l = head
        r = head
        prev = None
        counter = 0
        while r != None:
            r.prev = prev
            prev = r
            r = r.next
            counter += 1
        r = prev
        
        while counter != counter % 2:
            if l.val != r.val:
                return False
            l = l.next
            r = r.prev
            counter -= 2           
        return True