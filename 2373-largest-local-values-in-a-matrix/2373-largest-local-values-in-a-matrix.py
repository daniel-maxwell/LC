class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        
        def getMaxInSubGrid(coord):
            result = grid[coord[0]][coord[1]]
            for dr, dc in directions:
                newCoord = (coord[0] + dr, coord[1] + dc)
                result = max(result, grid[newCoord[0]][newCoord[1]])

            return result

        newGrid = [ [0] * (len(grid[0]) - 2) for _ in range(len(grid) - 2) ]

        for i in range(len(newGrid)):
            for j in range(len(newGrid[0])):
                newGrid[i][j] = getMaxInSubGrid((i+1, j+1))

        return newGrid