class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0],[0, 1],[1, 0],[0, -1]]
        visited = set()

        def isValidMove(coord):
            if (coord[0] < 0 or 
                coord[1] < 0 or 
                coord[0] == len(grid) or
                coord[1] == len(grid[0])):
                    return False
            return True

        def findAllLand():
            land = []
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        land.append((r,c))
                        visited.add((r, c))
            return land

        land = deque(findAllLand())
        if len(land) == 0 or len(land) == ROWS * COLS:
            return -1
        dist = 0

        while land:
            for _ in range(len(land)):
                curr = land.pop()
                for dr, dc in directions:
                    move = (curr[0] + dr, curr[1] + dc)
                    if isValidMove(move) and move not in visited:
                        land.appendleft(move)
                        visited.add(move)
            dist += 1

        return dist - 1