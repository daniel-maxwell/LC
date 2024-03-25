class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(0, len(grid)):
            grid[i] = [0] + grid[i] + [0]

        grid = [[0]* len(grid[0])] + grid + [[0]* len(grid[0])]

        perimiter = 0

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[1])-1):
                if grid[i][j] == 1:
                    perimiter += 4 - (grid[i-1][j] + grid[i+1][j] + grid[i][j-1] + grid[i][j+1])

        return perimiter