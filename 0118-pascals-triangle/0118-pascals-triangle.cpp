class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle = { {1} };
        for (int i = 1; i < numRows; ++i) {
            vector<int> row = { 1 };
            int lastRowIdx = triangle.size() - 1;
            for (int j = 1; j <= lastRowIdx; ++j) {
                row.push_back(triangle[lastRowIdx][j-1] + triangle[lastRowIdx][j]);
            };
            row.push_back(1);
            triangle.push_back(row);
        };
        return triangle;
    }; 
};