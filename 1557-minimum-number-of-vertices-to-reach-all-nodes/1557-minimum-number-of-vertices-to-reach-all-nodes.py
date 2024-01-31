class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = set()

        for i in range(n):
            vertices.add(i)

        for edge in edges:
            if edge[1] in vertices:
                vertices.remove(edge[1])

        return list(vertices)