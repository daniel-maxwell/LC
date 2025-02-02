class Solution {
public:
    const bool lemonadeChange(const vector<int>& bills) {
        unordered_map<int, int> billCounts {
            {5, 0},
            {10, 0},
            {20, 0}
        };
        for (const int &bill : bills) {
            ++billCounts[bill];
            if (bill == 10) {
                if (billCounts[5] < 1) {
                    return false;
                }
                --billCounts[5];
            } else if (bill == 20) {
                if (billCounts[5] < 1) {
                    return false;
                }
                if (billCounts[10] > 0) {
                    --billCounts[10];
                    --billCounts[5];
                } else {
                    if (billCounts[5] < 3) {
                        return false;
                    } else {
                        billCounts[5] -= 3;
                    }
                }

            }
        }
        return true;
    }
};