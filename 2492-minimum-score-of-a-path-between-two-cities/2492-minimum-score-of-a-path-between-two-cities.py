class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        cities = {}
        for start, end, dist in roads:
            if start in cities:
                cities[start].append((end, dist))
            else:
                cities[start] = [(end, dist)]

            if end in cities:
                cities[end].append((start, dist))
            else:
                cities[end] = [(start, dist)]

        minScore = float('inf')

        q = deque([1])
        visited = set([1])

        while q:
            curr = q.pop()
            for dest, score in cities[curr]:
                if dest not in visited:
                    q.appendleft(dest)
                    visited.add(dest)
                minScore = min(score, minScore)

        return minScore