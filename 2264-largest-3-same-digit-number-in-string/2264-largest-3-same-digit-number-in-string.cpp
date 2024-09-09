class Solution {
public:
    string largestGoodInteger(string num) {
        map<string, int> strMap {
            {"999", 9},
            {"888", 8},
            {"777", 7},
            {"666", 6},
            {"555", 5},
            {"444", 4},
            {"333", 3},
            {"222", 2},
            {"111", 1},
            {"000", 0},
            {"", -1}
        };
        string result = "";
        for (int i = 0; i < num.size(); ++i) {
            const string curr = num.substr(i, 3);
            if (strMap.contains(curr) && strMap[curr] > strMap[result]) {
                result = curr;
            }
        }
        return result;
    }
};