static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<int> currentRow = triangle[0];
        int rowCount = 1;
        while (rowCount < triangle.size()) {
            const int size = currentRow.size();
            vector<int> newRow(size + 1, 0);
            for (int i = 0; i < size; ++i) {
                newRow[i] = triangle[rowCount][i] + 
                    min(currentRow[i], i > 0 ? currentRow[i-1] : currentRow[i]);
            }
            newRow[newRow.size() - 1] = triangle[rowCount][size] + currentRow[size - 1];
            currentRow = newRow;
            ++rowCount;
        }
        return *min_element(currentRow.begin(), currentRow.end());
    }
};