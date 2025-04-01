class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> sortedMap;

        for (const string &s : strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            sortedMap[sortedS].push_back(s);
        }

        vector<vector<string>> result;

        for (const pair<string, vector<string>> &entry : sortedMap) {
            result.push_back(entry.second);
        }

        return result;
    }
};