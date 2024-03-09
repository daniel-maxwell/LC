class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while stones:
            y = abs(heapq.heappop(stones))
            
            if not stones:
                return y

            x = abs(heapq.heappop(stones))

            if y == x:
                continue

            elif y > x:
                y -= x
                heapq.heappush(stones, -y)

        return 0