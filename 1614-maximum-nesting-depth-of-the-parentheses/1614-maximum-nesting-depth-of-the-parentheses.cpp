class Solution {
public:
    const int maxDepth(const string s) {
        int maxDepth = 0;
        int curDepth = 0;
        for (const char &c : s) {
            if (c == '(') {
                ++curDepth;
                maxDepth = max(curDepth, maxDepth);
            } else if (c == ')') --curDepth;
        }
        return maxDepth;
    }
};