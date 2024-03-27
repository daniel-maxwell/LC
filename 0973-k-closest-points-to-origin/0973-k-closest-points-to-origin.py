class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = (0 - x)**2 + (0 - y)**2
            heap.append((dist, x, y))

        heapq.heapify(heap)

        res = []

        while len(res) < k:
            res.append(list(heapq.heappop(heap)[1:]))

        return res