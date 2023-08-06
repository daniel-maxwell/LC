# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head

        numNodes = 0
        curr = head
        data = []
        while curr != None:
            curr = curr.next
            numNodes += 1
            data.append(curr)

        middle = (numNodes // 2)
        return data[middle-1]