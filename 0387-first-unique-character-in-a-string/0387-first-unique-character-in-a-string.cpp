class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int>charCounts;
        for (const char c : s) {
            ++charCounts[c];
        }
        for (int i = 0; i < s.size(); ++i) {
            if (charCounts[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};