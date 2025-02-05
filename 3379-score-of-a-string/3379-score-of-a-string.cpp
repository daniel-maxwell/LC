class Solution {
public:
    const int scoreOfString(const string s) {
        int result = 0;
        for (int i = 0; i < s.size() - 1; ++i) {
            const int low = min(s[i] - 'a', s[i+1] - 'a');
            const int high = max(s[i] - 'a', s[i+1] - 'a');
            result += high - low;
        }
        return result;
    }
};