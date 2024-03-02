class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        if numRows == 1:
            return triangle

        numRows -= 1
        while numRows:
            row = []
            i = 0
            while i <= len(triangle[-1]):
                j = i - 1
                left = 0 if j < 0 else triangle[-1][j]
                right = 0 if i == len(triangle[-1]) else triangle[-1][i]
                row.append(left + right)
                i += 1
            triangle.append(row)
            numRows -= 1

        return triangle