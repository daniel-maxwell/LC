class Solution {
public:
    int twoSumLessThanK(vector<int>& nums, int k) {
        int result = -1;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; ++i) {
            int currMax = -1;
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] >= k) break;
                currMax = nums[i] + nums[j];
            }
            result = max(currMax, result);
        }
        return result;
    }
};