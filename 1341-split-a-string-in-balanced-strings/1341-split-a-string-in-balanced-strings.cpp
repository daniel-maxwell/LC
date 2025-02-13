class Solution {
public:
    int balancedStringSplit(string s) {
        int counter = 0;
        int ls = 0;
        int rs = 0;

        for (const char &c : s) {
            if (ls > 0 && ls == rs) {
                ++counter;
                ls = 0;
                rs = 0;
            }
            if (c == 'L') {
                ++ls;
            } else {
                ++rs;
            }
        }

        return counter + 1;
    }
};