static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    const bool searchMatrix(const vector<vector<int>>& matrix, const int target) {
        const int ROWS = matrix.size();
        const int COLS = matrix[0].size();
        int l = 0, r = ROWS * COLS - 1;
        while (l <= r) {
            const int mid = l + ((r - l) / 2);
            const pair<int, int> midCoord = convertTo2D(mid, COLS);
            const int cellValue = matrix[midCoord.first][midCoord.second];
            if (cellValue < target) l = mid + 1;
            else if (cellValue > target) r = mid - 1;
            else return true;
        }
        return false;
    }
private:
    const pair<int, int> convertTo2D(const int index1D, const int cols) {
        return pair<int, int> {index1D / cols, index1D % cols};
    }
};