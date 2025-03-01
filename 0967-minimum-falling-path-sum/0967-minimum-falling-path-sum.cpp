class Solution {
public:
    const int minFallingPathSum(const vector<vector<int>> &matrix) {
        vector<int> prevRow = matrix[0];
        int r = 1;
        while (r < matrix.size()) {
            vector<int> row;
            for (int c = 0; c < matrix.size(); ++c) {
                int minPrev;
                if (c == 0) {
                    minPrev = min(prevRow[c], prevRow[c + 1]);
                } else if (c == matrix.size() - 1) {
                    minPrev = min(prevRow[c - 1], prevRow[c]);
                } else {
                    minPrev = min(prevRow[c - 1], min(prevRow[c], prevRow[c + 1]));
                }
                row.push_back(minPrev + matrix[r][c]);
            }
            prevRow = row;
            ++r;
        }
        int result = 10001;
        for (const int &n : prevRow) {
            result = min(result, n);
        }
        return result;
    }
};