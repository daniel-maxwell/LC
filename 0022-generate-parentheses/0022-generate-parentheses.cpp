static const bool Init() {
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    const vector<string> generateParenthesis(const int n) {
        backtrack("", 0, 0, n);
        return result;
    }
private:
    void backtrack(const string &cur, const int open, const int close, const int n) {
        if (open == n && close == n) {
            result.push_back(cur);
            return;
        }
        if (close > open) return;
        if (open < n) {
            backtrack(cur + '(', open + 1, close, n);
            backtrack(cur + ')', open, close + 1, n);
        } else {
            backtrack(cur + ')', open, close + 1, n);
        }
    }
    vector<string> result;
};