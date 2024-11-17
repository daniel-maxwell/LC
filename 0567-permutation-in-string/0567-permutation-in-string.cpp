class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        unordered_map<char, int> s1Map;
        for (const char& c : s1) ++s1Map[c];

        unordered_map<char, int> s2Map;
        int l = 0;
        int r = 0;
        int matches = 0;

        // Create window of size s1.size()
        while (r < s2.size() && r - l < s1.size()) {
            ++s2Map[s2[r]];
            if (s1Map.contains(s2[r])) {
                if (s1Map[s2[r]] == s2Map[s2[r]]) {
                    ++matches;
                } else if (s1Map[s2[r]] == s2Map[s2[r]] - 1) {
                    --matches;
                }
            }
            ++r;
        }

        while (r < s2.size()) {
            if (matches == s1Map.size()) return true;

            --s2Map[s2[l]];
            if (s2Map[s2[l]] == 0) {
                s2Map.erase(s2[l]);
                if (s1Map.contains(s2[l]) && s1Map[s2[l]] == 1) {
                    --matches;
                }
            } else {
                if (s1Map.contains(s2[l])) {
                    if (s1Map[s2[l]] == s2Map[s2[l]]) {
                        ++matches;
                    } else if (s1Map[s2[l]] - 1 == s2Map[s2[l]]) {
                        --matches;
                    }
                }
            }
            ++l;

            ++s2Map[s2[r]];
            if (s1Map.contains(s2[r])) {
                if (s1Map[s2[r]] == s2Map[s2[r]]) {
                    ++matches;
                } else if (s1Map[s2[r]] + 1 == s2Map[s2[r]]) {
                    --matches;
                }
            }
            ++r;
        }

        return matches == s1Map.size();
    }
};