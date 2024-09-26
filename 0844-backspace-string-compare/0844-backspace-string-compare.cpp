static const bool a = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    bool backspaceCompare(const string s, const string t) {
        stack<char> sStack;
        stack<char> tStack;
        for (const char c : s) {
            if (c == '#') {
                if (!sStack.empty()) {
                    sStack.pop();
                }
            } else {
                sStack.push(c);
            }
        } 
        for (const char c : t) {
            if (c == '#') {
                if (!tStack.empty()) {
                    tStack.pop();
                }
            } else {
                tStack.push(c);
            }
        }
        return sStack == tStack;
    }
};