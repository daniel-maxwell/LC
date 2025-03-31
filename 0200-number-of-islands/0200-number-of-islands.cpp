class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        unordered_set<string> visited;
        vector<pair<int, int>> directions {
            {-1, 0}, {0, 1}, {1, 0}, {0, -1}
        };
        const int ROWS = grid.size();
        const int COLS = grid[0].size();
        int result = 0;

        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                const pair<int, int> coord{r, c};
                const string serialized = to_string(r) + "," + to_string(c);
                if (visited.contains(serialized)) continue;
                visited.insert(serialized);
                if (grid[r][c] == '0') continue;
                queue<pair<int, int>> q;
                q.push(coord);
                while (!q.empty()) {
                    const int length = q.size();
                    for (int _ = 0; _ < length; ++_) {
                        const pair<int, int> cur = q.front();
                        q.pop();
                        for (const pair<int, int> &dir : directions) {
                            const pair<int, int> dest {
                                cur.first + dir.first, cur.second + dir.second
                            };
                            const string serialized = 
                                to_string(dest.first) + "," + to_string(dest.second);
                            if (
                                dest.first >= 0 &&
                                dest.first < ROWS &&
                                dest.second >= 0 &&
                                dest.second < COLS &&
                                !visited.contains(serialized) &&
                                grid[dest.first][dest.second] == '1'
                            ) {
                                q.push(dest);
                                visited.insert(serialized);
                            }

                        }
                    }
                }
                ++result;
            }
        }
        return result;
    }
};