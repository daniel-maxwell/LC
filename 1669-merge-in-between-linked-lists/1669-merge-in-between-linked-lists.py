# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1

        while a > 1:
            start = start.next
            a -= 1
            b -= 1

        end = start.next
        b -= 1

        while b:
            end = end.next
            b -= 1
        
        start.next = list2
        curr = start.next

        while curr.next:
            curr = curr.next

        curr.next = end.next
        end.next = None

        return list1