class Solution {
public:
    int maxDepth(string s) {
        int maxDepth = 0;
        int curDepth = 0;
        for (char c : s) {
            if (c == '(') {
                ++curDepth;
            } else if (c == ')') {
                --curDepth;
            }
            maxDepth = max(curDepth, maxDepth);
        }
        return maxDepth;
    }
};