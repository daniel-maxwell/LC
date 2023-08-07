# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        curr = head.next
        prev = head

        while curr != None:
            duplicatesPresent = False
            
            while curr != None and prev.val == curr.val:
                duplicatesPresent = True
                curr = curr.next

            if duplicatesPresent == True:
                prev.next = curr

            if curr == None: break
            else:
                prev = curr
                curr = curr.next

        return head