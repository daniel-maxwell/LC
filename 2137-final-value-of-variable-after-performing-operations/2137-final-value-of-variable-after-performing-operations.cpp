class Solution {
public:
    const int finalValueAfterOperations(const vector<string>& operations) {
        int result = 0;
        for (const string &op : operations) {
            const char y = op[0] == '+' || op[0] == '-' ? op[0] : op[1];
            if (y == '+') ++result;
            else --result;
        }
        return result;
    }
};