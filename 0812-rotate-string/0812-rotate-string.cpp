class Solution {
public:
    const bool rotateString(const string s, const string goal) {
        if (s.size() != goal.size()) {
            return false;
        }
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == goal[0]) {
                if (s.substr(i, s.size()) + s.substr(0, i) == goal) {
                    return true;
                }
            }
        }
        return false;
    }
};