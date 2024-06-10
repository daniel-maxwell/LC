class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [[0] * len(matrix) for _ in matrix[0]]
        coord = [0, 0]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose[coord[0]][coord[1]] = matrix[i][j]
                coord[0] += 1
                if coord[0] == len(transpose):
                    coord[1] += 1
                    coord[0] = 0

        return transpose