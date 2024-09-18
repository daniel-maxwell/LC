static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int result = 0;
        while (!s.empty() && !g.empty()) {
            if (s.back() >= g.back()) {
                ++result;
                s.pop_back();
            }
            g.pop_back();
        }
        return result;
    }
};