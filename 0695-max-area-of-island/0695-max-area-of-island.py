class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited, res = set(), 0

        def getArea(r, c):
            if (r,c) in visited: return
            moves = []
            visited.add((r,c))
            currArea[0] += 1

            if r-1 >= 0 and (r-1,c) not in visited and grid[r-1][c] == 1:
                moves.append((r-1,c))
            if c+1 < len(grid[0]) and (r,c+1) not in visited and grid[r][c+1] == 1:
                moves.append((r,c+1))
            if r+1 < len(grid) and (r+1,c) not in visited and grid[r+1][c] == 1:
                moves.append((r+1,c))
            if c-1 >= 0 and (r,c-1) not in visited and grid[r][c-1] == 1:
                moves.append((r,c-1))

            if not moves: return 0

            while moves:
                r, c = moves.pop()
                getArea(r, c)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    currArea = [0]
                    getArea(i, j)
                    res = max(res, currArea[0])

        return res