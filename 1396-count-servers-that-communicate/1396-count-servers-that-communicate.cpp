class Solution {
public:
    const int countServers(const vector<vector<int>>& grid) {

        const int M = grid.size();
        const int N = grid[0].size();

        unordered_map<int, unordered_set<int>> connectedServers;

        for (int r = 0; r < M; ++r) {
            vector<int> cols;
            for (int c = 0; c < N; ++c) {
                if (grid[r][c] == 1) {
                    cols.push_back(c);
                }
            }
            if (cols.size() > 1) {
                for (const int &col : cols) {
                    connectedServers[r].insert(col);
                }
            }
        }

        for (int c = 0; c < N; ++c) {
            vector<int> rows;
            for (int r = 0; r < M; ++r) {
                if (grid[r][c] == 1) {
                    rows.push_back(r);
                }
            }
            if (rows.size() > 1) {
                for (const int &r : rows) {
                    connectedServers[r].insert(c);
                }
            }
        }

        int result = 0;

        for (const auto &entry : connectedServers) {
            result += entry.second.size();
        }

        return result;
    }
};