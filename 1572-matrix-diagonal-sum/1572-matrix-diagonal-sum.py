class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:        
        subtractMid = 0 if len(mat) % 2 == 0 else mat[len(mat)//2][len(mat)//2]

        offset = 0
        sum = 0

        for i in range(0, len(mat)):
            sum += mat[i][offset]
            sum += mat[i][0-(offset + 1)]
            offset += 1

        return sum - subtractMid