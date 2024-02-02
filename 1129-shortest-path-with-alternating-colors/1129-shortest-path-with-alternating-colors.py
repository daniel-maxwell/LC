class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = {}

        for edge in redEdges:
            if edge[0] not in graph: graph[edge[0]] = [(edge[1], "R")]
            else: graph[edge[0]].append((edge[1], "R"))
        for edge in blueEdges:
            if edge[0] not in graph: graph[edge[0]] = [(edge[1], "B")]
            else: graph[edge[0]].append((edge[1], "B"))

        res = []

        for target in range(n):
            visited, q = set((0, None)), deque([(0, None)])
            length, curr = 0, None
            found = False

            while q:
                if found: break
                for _ in range(len(q)):
                    curr = q.pop()
                    if curr[0] == target:
                        res.append(length)
                        found = True
                        break         
                    if curr[0] not in graph:
                        continue
                    for edge in graph[curr[0]]:
                        if edge not in visited and edge[1] != curr[1]:
                            q.appendleft(edge)
                            visited.add(edge)
                length += 1

            if not found:
                res.append(-1)

        return res