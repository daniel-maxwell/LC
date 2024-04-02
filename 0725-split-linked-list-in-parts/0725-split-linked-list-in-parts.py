# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        if not head:
            return [None for x in range(k)]

        curr, length = head, 0 

        while curr:
            length += 1
            curr = curr.next

        base_len, remainder = length // k, length % k
        curr, res = head, []

        for i in range(k):
            res.append(curr)
            for j in range((base_len - 1) + (1 if remainder else 0)):
                if not curr:
                    break
                curr = curr.next
            remainder -= (1 if remainder else 0)
            
            if curr:
                tmp = curr.next
                curr.next = None
                curr = tmp

        return res