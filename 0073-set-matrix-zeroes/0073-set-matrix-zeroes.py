class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        toConvert, convertedRows, convertedCols = [], set(), set()

        def convertRow(rowNum):
            for i in range(0, len(matrix[rowNum])):
                matrix[rowNum][i] = 0

        def convertCol(colNum):
            for row in matrix:
                row[colNum] = 0

        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[r])):
                if matrix[r][c] == 0:
                    toConvert.append((r, c))

        while toConvert:
            row, col = toConvert.pop()

            if row not in convertedRows:
                convertRow(row)
                convertedRows.add(row)

            if col not in convertedCols:
                convertCol(col)
                convertedCols.add(col)