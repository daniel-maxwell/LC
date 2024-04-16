class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def validatePlacement(board, coord):
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

            for DIR in directions:
                curr = coord
                while (
                    curr[0] >= 0 and
                    curr[0] < n and
                    curr[1] >= 0 and
                    curr[1] < n
                ):
                    if board[curr[0]][curr[1]] == 'Q':
                        return False

                    curr = [curr[0] + DIR[0], curr[1] + DIR[1]]

            return True

        board = []
        for _ in range(n):
            r = []
            for __ in range(n):
                r.append(".")
            board.append(r)

        res = []

        def backtrack(curr, board, remN):
            if not remN:
                res.append([''.join(row) for row in board])
                return

            if curr[1] == n:
                if board[curr[0]] == ["."] * n:
                    return
                curr[1] = 0
                curr[0] += 1

            if curr[0] >= n:
                return

            if validatePlacement(board, curr):
                newBoard = board.copy()
                newBoard[curr[0]][curr[1]] = 'Q'
                remN -= 1
                curr[1] += 1
                backtrack(curr.copy(), newBoard, remN)
                remN += 1

            else:
                curr[1] += 1

            board[curr[0]][curr[1] - 1] = "."
            backtrack(curr, board.copy(), remN)
         
        backtrack([0, 0], board, n)

        return res