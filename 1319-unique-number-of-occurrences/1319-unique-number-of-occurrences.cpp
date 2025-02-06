class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {

        unordered_map<int, int> numCounts;

        for (const int &n : arr) {
            ++numCounts[n];
        }

        unordered_set<int> occurences;

        for (const auto &entry : numCounts) {
            if (occurences.contains(entry.second)) {
                return false;
            }
            occurences.insert(entry.second);
        }

        return true;
    }
};