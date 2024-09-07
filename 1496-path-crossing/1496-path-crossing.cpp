class Solution {
public:
    bool isPathCrossing(string path) {
        map<char, pair<int, int>> directions {
            {'N', {-1, 0}},
            {'E', {0, 1}},
            {'S', {1, 0}},
            {'W', {0, -1}},
        };
        set<pair<int, int>> visited;
        pair<int, int> curr {0, 0};
        for (const char c : path) {
            visited.insert(curr);
            curr.first += directions[c].first;
            curr.second += directions[c].second;
            if (visited.contains(curr)) {
                return true;
            }
        }
        return false;
    }
};