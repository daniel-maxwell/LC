static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> s;
        for (const vector<string>& path : paths) {
            s.insert(path[0]);
        }
        for (const vector<string>& path : paths) {
            if (!s.contains(path[1])) {
                return path[1];
            }
        }
        return "";
    }
};