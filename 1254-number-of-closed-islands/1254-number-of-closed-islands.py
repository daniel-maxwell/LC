class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited, res = set(), 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def isValidMove(coord):
            if (coord[0] < 0 or
                coord[1] < 0 or
                coord[0] == ROWS or
                coord[1] == COLS):
                    return False
            return True

        def findFullIsland(coord):
            visited = set([coord])
            q = deque([coord])
            island = [coord]

            while q:
                for _ in range(len(q)):
                    curr = q.pop()
                    for dr, dc in directions:
                        move = (curr[0] + dr, curr[1] + dc)
                        if (move not in visited and 
                            isValidMove(move) and 
                            grid[move[0]][move[1]] == 0):
                                visited.add(move)
                                q.appendleft(move)
                                island.append(move)
            return island

        def isIslandSurrounded(island):
            for coord in island:
                for dr, dc in directions:
                    move = (coord[0] + dr, coord[1] + dc)
                    if not isValidMove(move):
                        return False
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited: continue
                if grid[r][c] == 0:
                    isl = findFullIsland((r, c))
                    visited.update(isl)
                    if isIslandSurrounded(isl):
                        res += 1
        return res