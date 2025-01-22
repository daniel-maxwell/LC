class Solution {
public:
    const int sumOfDigits(const vector<int>& nums) {
        int MIN = 101;
        for (const int &n : nums) MIN = min(MIN, n);
        int result = 0;
        while (MIN > 0) {
            result += MIN % 10;
            MIN /= 10;
        }
        return result % 2 == 0 ? 1 : 0;
    }
};