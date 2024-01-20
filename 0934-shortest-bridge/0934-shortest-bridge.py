class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid) - 1
        directions = [[-1, 0],[0, 1],[1, 0],[0, -1]]

        def isValidMove(coord, visited):
            if (coord[0] < 0 or coord[1] < 0
            or coord[0] == len(grid) or
            coord[1] == len(grid[0]) or
            coord in visited):
                return False
            return True

        def findFirstIsland(coord):
            visited = set([coord])
            q = deque([coord])
            res = [coord]

            while q:
                for _ in range(len(q)):
                    curr = q.pop()
                    for dr, dc in directions:
                        move = (curr[0] + dr, curr[1] + dc)
                        if (isValidMove(move, visited)
                        and grid[move[0]][move[1]] == 1):
                            q.appendleft(move)
                            visited.add(move)
                            res.append(move)
            return res

        def distToSecondIsland(coords):
            visited = set(coords)
            q = deque(coords)
            dist = 0

            while q:
                for _ in range(len(q)):
                    curr = q.pop()
                    for dr, dc in directions:
                        move = (curr[0] + dr, curr[1] + dc) 
                        if isValidMove(move, visited):
                            if grid[move[0]][move[1]] == 0:
                                q.appendleft(move)
                                visited.add(move)
                            else:
                                return dist
                dist += 1
            return -1

        firstIsland = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    firstIsland = findFirstIsland((r, c))
                    break
            if firstIsland: break

        return distToSecondIsland(firstIsland)