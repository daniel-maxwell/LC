class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRows(board):
            for row in board:
                rowSet = set()
                for el in row:
                    if el.isdigit():
                        if el in rowSet:
                            return False
                        rowSet.add(el)
            return True

        def checkCols(board):
            for col in range(0, 9):
                rowNum = 0
                colSet = set()
                while rowNum < 9:
                    el = board[rowNum][col]
                    if el.isdigit():
                        if el in colSet:
                            return False
                        colSet.add(el)
                    rowNum += 1
            return True

        def checkSubBoxes(board):
            rowNum = 0         
            while rowNum <= 6:
                colNum = 0
                while colNum <= 6:
                    boxSet = set()
                    for i in range(0, 3):
                        for j in range(0, 3):
                            el = board[rowNum+i][colNum+j]
                            if el.isdigit():
                                if el in boxSet:
                                    return False
                                boxSet.add(el)
                    colNum += 3
                rowNum += 3
            return True

        return checkRows(board) and checkCols(board) and checkSubBoxes(board)