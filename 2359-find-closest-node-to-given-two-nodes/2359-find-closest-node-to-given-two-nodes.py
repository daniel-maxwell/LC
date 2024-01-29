class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1Dists, node2Dists = {}, {}

        def getDistances(node, distdict):
            visited = set()
            curr = node
            dist = 0
            while curr not in visited:
                if curr == -1: break
                visited.add(curr)
                distdict[curr] = dist
                curr = edges[curr]
                dist += 1
            return distdict

        node1Dists = getDistances(node1, {})
        node2Dists = getDistances(node2, {})

        res = [float('inf'), float('inf')] # dist, index

        for idx, dist in node1Dists.items():
            if idx in node2Dists:
                if max(dist, node2Dists[idx]) < res[0]:
                    res = [max(dist, node2Dists[idx]), idx]
                elif max(dist, node2Dists[idx]) == res[0]:
                    if idx < res[1]:
                        res = [max(dist, node2Dists[idx]), idx]

        return res[1] if res[1] != float('inf') else -1