class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        def shiftOnce(grid):
            prev = grid[-1][-1]

            i = 0

            while i < len(grid):

                for j in range(0, len(grid[i])):

                    tmp = grid[i][j]
                    grid[i][j] = prev
                    prev = tmp

                i += 1

            return grid

        for i in range(0, k):
            grid = shiftOnce(grid)

        return grid