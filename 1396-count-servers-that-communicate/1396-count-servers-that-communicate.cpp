class Solution {
public:
    int countServers(vector<vector<int>>& grid) {

        const int M = grid.size();
        const int N = grid[0].size();

        unordered_set<string> connectedServers;

        for (int r = 0; r < M; ++r) {
            vector<string> serversInRow;
            for (int c = 0; c < N; ++c) {
                if (grid[r][c] == 1) {
                    serversInRow.push_back(to_string(r) + "," + to_string(c));
                }
            }
            if (serversInRow.size() > 1) {
                for (const string &coord : serversInRow) {
                    connectedServers.insert(coord);
                }
            }
        }

        for (int c = 0; c < N; ++c) {
            vector<string> serversInCol;
            for (int r = 0; r < M; ++r) {
                if (grid[r][c] == 1) {
                    serversInCol.push_back(to_string(r) + "," + to_string(c));
                }
            }
            if (serversInCol.size() > 1) {
                for (const string &coord : serversInCol) {
                    connectedServers.insert(coord);
                }
            }
        }

        return connectedServers.size();
    }
};