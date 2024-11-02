auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class NumMatrix {
public:
    NumMatrix(const vector<vector<int>>& matrix) {
        const int rows = matrix.size();
        const int cols = matrix[0].size();
        sumMatrix = vector<vector<int>>(rows + 1, vector<int>(cols + 1, 0));
        for (size_t i = 1; i <= rows; ++i) {
            for (size_t j = 1; j <= cols; ++j) {
                sumMatrix[i][j] = matrix[i - 1][j - 1]
                + sumMatrix[i - 1][j]
                + sumMatrix[i][j - 1]
                - sumMatrix[i - 1][j - 1];
            }
        }
    }
    
    const int sumRegion(const int row1, const int col1, const int row2, const int col2) {
        return (
            sumMatrix[row2+1][col2+1]
            - sumMatrix[row1][col2+1]
            - sumMatrix[row2+1][col1]
            + sumMatrix[row1][col1]
        );
    }

private:
    vector<vector<int>> sumMatrix;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */