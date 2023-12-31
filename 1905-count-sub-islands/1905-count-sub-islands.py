class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited, res, ROWS, COLS = set(), 0, len(grid1), len(grid1[0])

        def checkIsland(r, c):
            if grid1[r][c] != 1: return False
            if (r,c) in visited: return True
            moves = []
            visited.add((r,c))

            if r-1 >= 0 and (r-1,c) not in visited and grid2[r-1][c] == 1:
                moves.append((r-1,c))
            if c+1 < COLS and (r,c+1) not in visited and grid2[r][c+1] == 1:
                moves.append((r,c+1))
            if r+1 < ROWS and (r+1,c) not in visited and grid2[r+1][c] == 1:
                moves.append((r+1,c))
            if c-1 >= 0 and (r,c-1) not in visited and grid2[r][c-1] == 1:
                moves.append((r,c-1))

            if not moves: return True
            valid = True
            while moves:
                r, c = moves.pop()
                if not checkIsland(r, c) and valid: valid = False
            return valid

        for i in range(0, len(grid2)):
            for j in range(0, len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    if checkIsland(i, j): res += 1
        return res