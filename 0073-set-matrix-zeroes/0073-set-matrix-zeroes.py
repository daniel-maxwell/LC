class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowsToConvert, colsToConvert = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsToConvert.add(i)
                    colsToConvert.add(j)

        for row in range(len(matrix)):
            if row in rowsToConvert:
                matrix[row] = [0] * len(matrix[row])

            for col in range(len(matrix[0])):
                if col in colsToConvert:
                    for r in matrix:
                        r[col] = 0

        return matrix