class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int numOperations = 0;
        int i = 0, j = nums.size() - 1;
        long long left = static_cast<long long>(nums[i]);
        long long right = static_cast<long long>(nums[j]);
        while (i < j) {
            if (left == right) {
                ++i;
                --j;
                left = static_cast<long long>(nums[i]);
                right = static_cast<long long>(nums[j]);
                continue;
            }
            if (left < right) {
                left = static_cast<long long>(nums[i + 1]) + static_cast<long long>(nums[i]);
                ++i;
            } else {
                right = static_cast<long long>(nums[j - 1]) + static_cast<long long>(nums[j]);
                --j;
            }
            ++numOperations;
        }
        return numOperations;
    }
};