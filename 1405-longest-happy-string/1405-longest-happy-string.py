class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts, letters = [-a, -b, -c], ["a", "b", "c"]
        maxHeap = [list(t) for t in zip(counts, letters) if t[0] < 0]
        heapq.heapify(maxHeap)
        prev, res = None, []

        while len(maxHeap) > 1:
            top = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            if abs(top[0]) - abs(second[0]) >= 2:
                res.append(2 * top[1])
                top[0] += 2
                res.append(second[1])
                second[0] += 1

            else:
                res.append(top[1])
                top[0] += 1
                res.append(second[1])
                second[0] += 1

            if top[0] <= -1: heapq.heappush(maxHeap, top)
            if second[0] <= -1: heapq.heappush(maxHeap, second)
        
        if maxHeap:
            last = heapq.heappop(maxHeap)
            if last[0] < -1:
                return ''.join(res) + (2 * last[1])
            else:
                return ''.join(res) + last[1]
        else:
            return ''.join(res)