class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<int> hashed_s = {}, hashed_t = {};

        for (int i = 0; i < s.size(); ++i) {
            int idx_s = -1, idx_t = -1;

            for (int j = 0; j < s.size(); ++j) {
                if (s[i] == s[j] && idx_s == -1) idx_s = j;
                if (t[i] == t[j] && idx_t == -1) idx_t = j;
                if (idx_s != -1 && idx_t != -1) break;
            };
            hashed_s.push_back(idx_s);
            hashed_t.push_back(idx_t);
        };
        return hashed_s == hashed_t;
    };
};