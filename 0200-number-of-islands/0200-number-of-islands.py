class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited, counter = set(), 0

        def findCompleteIsland(pos):
            if grid[pos[0]][pos[1]] != "1": return
            visited.add(pos)
            moves = []
            row, col = pos

            if row-1 >= 0 and (row-1, col) not in visited: # Top
                moves.append((row-1, col))
            if col+1 < len(grid[0]) and (row, col+1) not in visited: # Right
                moves.append((row, col+1))
            if row+1 < len(grid) and (row+1, col) not in visited: # Bottom
                moves.append((row+1, col))
            if col-1 >= 0 and (row, col-1) not in visited: # Left
                moves.append((row, col-1))

            while moves:
                findCompleteIsland(moves.pop())
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if (i, j) in visited: continue
                visited.add((i, j))
                if grid[i][j] == "1":
                    findCompleteIsland((i, j))
                    counter += 1
        
        return counter