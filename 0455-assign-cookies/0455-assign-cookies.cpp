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