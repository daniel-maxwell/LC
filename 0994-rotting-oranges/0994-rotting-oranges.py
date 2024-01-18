class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = set()
        ROWS, COLS = len(grid), len(grid[0])
        moveDiffs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        # populates the rotten and fresh orange data structures
        r, c = 0, 0
        while r < ROWS:
            if grid[r][c] == 1:
                fresh.add((r, c))
            elif grid[r][c] == 2:
                rotten.appendleft((r, c))
            c += 1
            if c == COLS:
                r += 1
                c = 0

        def isValidMove(coord):
            if (coord[0] < 0 or coord[1] < 0 or 
            coord[0] == ROWS or coord[1] == COLS or
            coord not in fresh):
                return False
            return True
        
        counter = 0
        
        while rotten: 
            if not fresh: return counter
            for _ in range(0, len(rotten)):
                curr = rotten.pop()
                for rDiff, cDiff in moveDiffs:
                    move = (curr[0] + rDiff, curr[1] + cDiff)
                    if isValidMove(move):
                        rotten.appendleft(move)
                        fresh.remove(move)
                        
            counter += 1           

        return -1 if fresh else counter