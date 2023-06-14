class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = []
        numEls = 1
        for i in range(0, numRows):
            for j in range(0, numEls):
                if j==0 or j==numEls-1: row.append(1)
                else:
                    row.append(triangle[-1][j-1] + triangle[-1][j])    
            numEls+=1
            triangle+=[row]
            row = []
        return triangle