# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr, carry = head, False

        while True:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            if carry:
                sum += 1
                carry = False

            if sum <= 9:
                curr.val = sum

            else:
                carry = True
                curr.val = sum % 10

            if not (l1 or l2):
                if carry:
                    curr.next = ListNode(1)
                break

            curr.next = ListNode()
            curr = curr.next

        return head