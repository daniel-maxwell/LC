class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board) - 1
        visited, regions = set(), []
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def isValidMove(move):
            if (move[0] < 0 or move[1] < 0
            or move[0] == len(board) or 
            move[1] == len(board[0])):
                return False
            return True

        def getFullRegion(coord):
            q = deque([coord])
            region = [coord]
            visit = set([coord])
            while q:
                for _ in range(len(q)):
                    curr = q.pop()
                    for dr, dc in directions:
                        move = (curr[0] + dr, curr[1] + dc)
                        if (move not in visit 
                        and isValidMove(move) 
                        and board[move[0]][move[1]] == 'O'):
                            q.appendleft(move)
                            region.append(move)
                        visit.add(move)
            return region

        def checkSurroundingRegion(region):
            visit = set(region)
            for i in range(len(region)):
                for dr, dc in directions:
                    move = (region[i][0] + dr, region[i][1] + dc)
                    if move in visit:
                        continue
                    if not isValidMove(move):
                        return False
            return True

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) in visited: continue
                if board[r][c] == 'O':
                    region = getFullRegion((r, c))
                    visited.update(set(region))
                    if checkSurroundingRegion(region):
                        for i, j in region:
                            board[i][j] = 'X'