# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        minHeap, nodesToDelete = [], set()
        heapq.heapify(minHeap)

        i, ptr = 0, head
        while ptr:
            while minHeap and minHeap[0][0] < ptr.val:
                nodesToDelete.add(heapq.heappop(minHeap)[2])
            heapq.heappush(minHeap, [ptr.val, i, ptr])
            ptr = ptr.next
            i += 1

        ptr, prev = head, ListNode(0, head)

        while ptr:
            if ptr in nodesToDelete:
                if ptr == head:
                    head = head.next
                prev.next = ptr.next
                ptr.next = None
                ptr = prev.next

            else:
                prev = ptr
                ptr = ptr.next

        return head