class Solution {
public:
    const vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        const int originalColor = image[sr][sc];
        queue<pair<int, int>> q;
        q.push(pair<int, int>{sr, sc});
        const vector<pair<int, int>> directions {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        unordered_set<string> visited;
        while (!q.empty()) {
            const int length = q.size();
            for (int _ = 0; _ < length; ++_) {
                const pair<int, int> cur = q.front();
                q.pop();
                image[cur.first][cur.second] = color;
                for (const pair<int, int>& dir : directions) {
                    const pair<int, int> move {cur.first + dir.first, cur.second + dir.second};
                    const string strMove = to_string(move.first) + "," + to_string(move.second);
                    if (move.first >= 0 &&
                        move.first < image.size() &&
                        move.second >= 0 &&
                        move.second < image[0].size() &&
                        !visited.contains(strMove) &&
                        image[move.first][move.second] == originalColor
                    ) {
                        q.push(move); 
                        visited.insert(strMove);
                    }
                }
            }
        }
        return image;
    }
};