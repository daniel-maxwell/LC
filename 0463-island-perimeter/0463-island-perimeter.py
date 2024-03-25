class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def isValidMove(coord):
            if (
                coord[0] < 0 or
                coord[0] >= ROWS or
                coord[1] < 0 or
                coord[1] >= COLS or
                grid[coord[0]][coord[1]] == 0
            ):
                return False
            else:
                return True

        def getPerimiter(coord):
            visited = set([coord])
            perimiter = 0
            q = deque([coord])
            
            while q:
                curr = q.pop()
                for dc, dr in directions:
                    move = (curr[0] + dc, curr[1] + dr)

                    if isValidMove(move):
                        if move not in visited:
                            q.appendleft(move)
                    else:
                        perimiter += 1

                    visited.add(move)
            return perimiter
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return getPerimiter((i, j))