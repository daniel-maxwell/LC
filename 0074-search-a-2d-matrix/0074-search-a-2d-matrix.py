class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def convert1Dto2D(val, rows, cols):
            r = val // cols
            c = val % cols
            return(r, c)

        l, r = 0, (len(matrix) * len(matrix[0])) -1

        while l <= r:
            mid = l + ((r-l) // 2)

            row, col = convert1Dto2D(mid, len(matrix), len(matrix[0]))

            if matrix[row][col] < target: l = mid + 1

            elif matrix[row][col] > target: r = mid - 1

            else: return True

        return False