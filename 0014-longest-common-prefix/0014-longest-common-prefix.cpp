class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int j = 0;
        char c = strs[0][0];
        while (j < strs[0].size()) {
            for (int i = 0; i < strs.size(); ++i) {
                if (j == strs[i].size() || strs[i][j] != c) return strs[0].substr(0, j);
            };
            ++j;
            c = strs[0][j];
        };
        return strs[0].substr(0, j);
    };
};