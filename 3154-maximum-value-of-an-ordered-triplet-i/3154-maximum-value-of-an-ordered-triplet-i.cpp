class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long result = -1;

        vector<int> maxRight(nums.size(), 0);

        int curMax = nums.back();
        for (int i = nums.size() - 1; i >= 0; --i) {
            maxRight[i] = curMax;
            curMax = max(curMax, nums[i]);
        }

        for (int i = 0; i < nums.size() - 2; ++i) {
            for (int j = i + 1; j < nums.size() - 1; ++j) {
                result = max(result, (static_cast<long long>(nums[i]) - static_cast<long long>(nums[j])) * static_cast<long long>(maxRight[j]));
            }
        }

        return result > 0 ? result : 0;   
    }
};