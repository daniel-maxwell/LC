class Solution {
public:
    string largestGoodInteger(string num) {
        set<string> strSet {"999","888", "777", "666", "555", "444", "333", "222", "111", "000"};
        string result = "";
        for (int i = 0; i < num.size(); ++i) {
            const string curr = num.substr(i, 3);
            if (strSet.contains(curr) && curr > result) {
                result = curr;
            }
        }
        return result;
    }
};