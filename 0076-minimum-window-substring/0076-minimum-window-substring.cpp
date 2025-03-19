class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> sCharCounts;
        unordered_map<char, int> tCharCounts;

        for (const char &c : s) {
            ++sCharCounts[c];
        }

        for (const char &c : t) {
            ++tCharCounts[c];
        }

        for (const auto &entry : tCharCounts) {
            if (!sCharCounts.contains(entry.first) || sCharCounts[entry.first] < entry.second) {
                return "";
            }
        }

        string result = "";
        int minSize = s.size() + 1;
        int l = 0, r = s.size() - 1;

        while (r < s.size()) {
            // Decrement r until substring is invalid
            while (r - l >= t.size()) {
                if (tCharCounts.contains(s[r]) && (sCharCounts[s[r]] == tCharCounts[s[r]])) { // Stop
                    break;
                }
                --sCharCounts[s[r]];
                --r;
            }

            // Increment l until substring is invalid
            while (r - l >= t.size()) {
                if (tCharCounts.contains(s[l]) && (sCharCounts[s[l]] == tCharCounts[s[l]])) { // Stop
                    break;
                }
                --sCharCounts[s[l]];
                ++l;
            }

            if (r - l + 1 < minSize) result = s.substr(l, r - l + 1);

            int matchingChars = t.size() - 1;

            --sCharCounts[s[l]];
            ++l;
            ++r;
            if (r < s.size()) {
                ++sCharCounts[s[r]];
                if (tCharCounts.contains(s[r]) && tCharCounts[s[r]] == sCharCounts[s[r]]) {
                    ++matchingChars;
                }
            }
            while (r < s.size() && matchingChars < t.size()) {
                if (tCharCounts.contains(s[l]) && tCharCounts[s[l]] == sCharCounts[s[l]]) {
                    --matchingChars;
                }
                --sCharCounts[s[l]];
                ++l;
                ++r;
                if (r < s.size()) {
                    ++sCharCounts[s[r]];
                    if (tCharCounts.contains(s[r]) && tCharCounts[s[r]] == sCharCounts[s[r]]) {
                        ++matchingChars;
                    }
                }
            }
        }

        return result;
    }
};