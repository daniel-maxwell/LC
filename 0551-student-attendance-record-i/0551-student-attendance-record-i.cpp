class Solution {
public:
    const bool checkRecord(const string s) {
        int remAbsences = 1;
        int consecutiveLates = 0;
        for (const char &c : s) {
            if (c == 'A') {
                --remAbsences;
                if (remAbsences == -1) {
                    return false;
                }
                consecutiveLates = 0;
            } else if (c == 'L') {
                ++consecutiveLates;
                if (consecutiveLates == 3) {
                    return false;
                }
            } else {
                consecutiveLates = 0;
            }
        }
        return true;
    }
};