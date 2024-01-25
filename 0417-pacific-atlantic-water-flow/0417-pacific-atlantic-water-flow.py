class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0],[0, 1],[1, 0],[0, -1]]
        visited = set()

        def isValidMove(coord):
            if (coord[0] < 0 or 
                coord[1] < 0 or 
                coord[0] == ROWS or
                coord[1] == COLS):
                    return False
            return True

        def flowsToOcean(coords):
            visited = set(coords)
            res = set(coords)
            q = deque(coords)
            
            while q:
                for _ in range(len(q)):
                    curr = q.pop()
                    for dr, dc in directions:
                        move = (curr[0] + dr, curr[1] + dc)
                        if (isValidMove(move) and 
                            move not in visited and
                            heights[move[0]][move[1]] >= heights[curr[0]][curr[1]]):
                                res.add(move)
                                visited.add(move)
                                q.appendleft(move)
            return res

        pacificCoast = []
        atlanticCoast = []

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacificCoast.append((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    atlanticCoast.append((r, c))

        return list(flowsToOcean(pacificCoast).intersection(flowsToOcean(atlanticCoast)))