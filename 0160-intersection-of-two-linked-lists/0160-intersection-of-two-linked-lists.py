# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeSet = set()
        currA = headA
        currB = headB

        while currA and currB:
            if currA in nodeSet:
                return currA
            nodeSet.add(currA)
            currA = currA.next

            if currB in nodeSet:
                return currB
            nodeSet.add(currB)                 
            currB = currB.next
     
        while currA:
            if currA in nodeSet:
                return currA
            nodeSet.add(currA)
            currA = currA.next

        while currB:
            if currB in nodeSet:
                return currB
            nodeSet.add(currB)
            currB = currB.next

        return None