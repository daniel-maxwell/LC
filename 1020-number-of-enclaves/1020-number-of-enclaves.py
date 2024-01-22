class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        land, visited, q = set(), set(), deque()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if (r == 0 
                    or r == ROWS - 1 
                    or c == 0 
                    or c == COLS - 1):
                        q.appendleft((r, c))
                        visited.add((r, c))                   
                    else:
                        land.add((r, c))

        def isValidMove(coord):
            if (coord[0] < 0
            or coord[1] < 0
            or coord[0] == ROWS
            or coord[1] == COLS
            or coord in visited):
                return False
            return True
        
        while q:
            for _ in range(len(q)):
                curr = q.pop()
                for dr, dc in directions:
                    move = (curr[0] + dr, curr[1] + dc)
                    if isValidMove(move) and move in land:
                        land.remove(move)
                        q.appendleft(move)
                        visited.add(move)

        return len(land)