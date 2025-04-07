class Solution {
public:
    const string kthDistinct(const vector<string>& arr, int k) {
        unordered_map<string, int> strCounts;

        for (const string &s : arr) {
            ++strCounts[s];
        }

        int distinctCount = 0;

        for (const string &s : arr) {
            if (strCounts[s] == 1) {
                ++distinctCount;
                if (distinctCount == k) return s;
            }
        }

        return "";
    }
};