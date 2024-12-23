class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        unordered_set<char> digits {
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        };

        vector<pair<string, string>> letterLogs;
        vector<string> digitLogs;

        for (int i = 0; i < logs.size(); ++i) {
            const size_t firstSpace = logs[i].find(' ');
            if (digits.contains(logs[i][firstSpace + 1])) {
                digitLogs.push_back(logs[i]);
            } else {
                letterLogs.push_back(pair<string, string>{logs[i].substr(firstSpace + 1), logs[i]});
            }
        }

        sort(letterLogs.begin(), letterLogs.end());
        vector<string> result(logs.size(), "");

        for (int i = result.size() - 1; i >= 0; --i) {
            if (!digitLogs.empty()) {
                result[i] = digitLogs.back();
                digitLogs.pop_back();
            } else {
                result[i] = letterLogs.back().second;
                letterLogs.pop_back();
            }
        }

        return result;
    }
};