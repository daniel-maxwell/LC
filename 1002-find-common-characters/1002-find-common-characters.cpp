class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        unordered_map<char, int> minCharCounts;

        for (const char &c : words[0]) {
            ++minCharCounts[c];
        }

        for (int i = 1; i < words.size(); ++i) {
            unordered_map<char, int> charCounts;
            for (const char &c : words[i]) {
                ++charCounts[c];
            }
            for (const auto& entry : minCharCounts) {
                if (!charCounts.contains(entry.first)) {
                    minCharCounts[entry.first] = 0;
                } else {
                    minCharCounts[entry.first] = min(minCharCounts[entry.first], charCounts[entry.first]);
                }
            }
        }

        vector<string> result;

        for (const auto& entry : minCharCounts) {
            for (int i = 0; i < entry.second; ++i) {
                result.push_back(string(1, entry.first));
            }
        }

        return result;
    }
};