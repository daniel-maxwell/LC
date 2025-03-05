
class Solution {
public:
    const bool searchMatrix(const vector<vector<int>>& matrix, const int target) {
        ROWS = matrix.size();
        COLS = matrix[0].size();
        int l = 0;
        int r = (ROWS * COLS) - 1;
        while (l <= r) {
            const int mid = l + ((r - l) / 2);
            const pair<int, int> midCoord = convert1DTo2D(mid);
            const int value = matrix[midCoord.first][midCoord.second];
            if (value > target) {
                r = mid - 1;
            } else if (value < target) {
                l = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
private:
    const pair<int, int> convert1DTo2D(int index) {
        if (index == 0) return pair<int, int>{0, 0};
        return pair<int, int>{index / COLS, index % COLS};
    }
    int ROWS;
    int COLS;
};