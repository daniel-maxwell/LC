class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int ROWS = matrix.size();
        const int COLS = matrix[0].size();

        unordered_set<string> visited;

        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (r == c) continue;
                const string cStr = to_string(c);
                const string rStr = to_string(r);
                const string curCoords = cStr + "," + rStr;
                const string oppCoords = rStr + "," + cStr;
                if (visited.contains(curCoords)) continue;
                visited.insert(oppCoords);
                const int temp = matrix[c][r];
                matrix[c][r] = matrix[r][c];
                matrix[r][c] = temp;
            }
        }

        for (int i = 0; i < matrix.size(); ++i) {
            int l = 0;
            int r = matrix[i].size() - 1;
            while (l < r) {
                int temp = matrix[i][l];
                matrix[i][l] = matrix[i][r];
                matrix[i][r] = temp;
                ++l;
                --r;
            }
        }
    }
};