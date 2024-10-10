auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const int maxScore(const string s) {
        int result = 0;
        int maxRight = 0;
        int maxLeft = 0;
        for (const char& c : s) if (c == '1') ++maxRight;
        for (int i = 0; i < s.size() - 1; ++i) {
            if (s[i] == '1') --maxRight;
            else ++maxLeft;
            result = max(result, maxLeft + maxRight);
        }
        return result;
    }
};