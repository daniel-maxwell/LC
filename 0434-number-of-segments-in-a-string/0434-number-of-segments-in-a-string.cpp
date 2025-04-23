class Solution {
public:
    int countSegments(string s) {
        int i = 0;
        int result = 0;
        while (i < s.size()) {
            if (s[i] != ' ') {
                ++result;
                while (i < s.size() && s[i] != ' ') {
                    ++i;
                }
            }
            ++i;
        }
        return result;
    }
};