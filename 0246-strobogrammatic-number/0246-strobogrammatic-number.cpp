class Solution {
public:
    bool isStrobogrammatic(string num) {
        const unordered_map<int, int> mappings {
            {'0', '0'},
            {'1', '1'},
            {'6', '9'},
            {'8', '8'},
            {'9', '6'}
        };
        string rotatedNum = "";
        for (const char &digit : num) {
            if (!mappings.contains(digit)) return false;
            rotatedNum += mappings.at(digit);
        }
        reverse(rotatedNum.begin(), rotatedNum.end());
        return rotatedNum == num;
    }
};