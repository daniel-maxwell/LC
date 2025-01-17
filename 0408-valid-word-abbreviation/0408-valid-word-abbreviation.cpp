class Solution {
public:
    const bool validWordAbbreviation(const string word, const string abbr) {
        const unordered_set<char> digits {
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        };
        int i = 0, j = 0;
        while (i < word.size()) {
            string strNum = "";
            while (j < abbr.size() && digits.contains(abbr[j])) {
                strNum += abbr[j];
                ++j;
            }
            if (strNum.size() >= 1) {
                if (strNum[0] == '0') return false;
                const int jumpLength = stoi(strNum);
                if (jumpLength > word.size() - i) return false;
                i += jumpLength;
            } else {
                if (i < word.size() && j < abbr.size()) {
                    if (word[i] != abbr[j]) return false;
                } else if (i < word.size() || j < abbr.size()) return false;
                ++i;
                ++j;
            }
        };
        return j == abbr.size();
    }
};