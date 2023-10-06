import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        diffMinHeap = []
        output = []

        for val in arr:
            diff = abs(x - val)
            heapq.heappush(diffMinHeap, (diff, val))

        while len(output) < k:
            output.append(heapq.heappop(diffMinHeap)[1])

        output.sort()

        return output