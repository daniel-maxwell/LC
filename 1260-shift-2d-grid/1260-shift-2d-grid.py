class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        # Get the dimensions of the grid
        M, N = len(grid), len(grid[0])

        ### Helper functions ###
        
        # Converts the position in the grid to position in 1D array
        def posToVal(r, c):
            return r * N + c

        # Converts the idx in a 1D array to position in the grid
        def valToPos(v):
            return [v//N, v % N]

        # Create (currently 0-filled) result grid
        res = [[0] * N for i in range(M)]

        # iterate through every position in the 2D grid
        for r in range(M):
            for c in range(N):
                # Calculate value in 1D array
                newVal = (posToVal(r, c) + k) % (M * N)

                # Calculate new position in result grid
                newR, newC = valToPos(newVal)

                # Insert value in to result grid
                res[newR][newC] = grid[r][c]

        return res