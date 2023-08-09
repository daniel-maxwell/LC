# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            return list1 if list1 else list2
        
        output = None

        if list1.val <= list2.val:
            output = ListNode(val=list1.val, next=None)
            list1 = list1.next
        else:
            output = ListNode(val=list2.val, next=None)
            list2 = list2.next

        currOutput = output

        while list1 and list2:
            if list1.val < list2.val:
                currOutput.next = ListNode(val = list1.val, next=None)
                list1 = list1.next
                currOutput = currOutput.next

            else:
                currOutput.next = ListNode(val = list2.val, next=None)
                list2 = list2.next
                currOutput = currOutput.next
        
        if list1: currOutput.next = list1
        else: currOutput.next = list2

        return output