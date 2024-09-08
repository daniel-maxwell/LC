class Solution {
public:
    bool makeEqual(vector<string>& words) {
        map<char, int> charCounts;
        for (auto const &word : words) {
            for (const char c : word) {
                ++charCounts[c];
            }
        }
        for (auto const &[key, val] : charCounts) {
            if (val % words.size() != 0) {
                return false;
            }
        }
        return true;
    }
};