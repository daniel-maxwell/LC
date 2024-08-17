class Solution {
public:
    string frequencySort(std::string s) {
        std::unordered_map<char, int> frequencies;
        for (char c : s) {
            frequencies[c]++;
        }
        std::vector<std::pair<char, int>> charFreq(frequencies.begin(), frequencies.end());
        std::sort(charFreq.begin(), charFreq.end(), [](const auto &a, const auto &b) {
            return a.second > b.second;
        });
        std::string result;
        for (const auto &pair : charFreq) {
            result += std::string(pair.second, pair.first);
        }
        return result;
    };
  };
