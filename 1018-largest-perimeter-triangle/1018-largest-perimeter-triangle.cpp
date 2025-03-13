class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int result = 0;
        for (int i = 0; i < nums.size() - 2; ++i) {
            for (int j = i + 2; j < nums.size(); ++j) {
                if (nums[i] + nums[i+1] > nums[j]) {
                    result = max(result, nums[i] + nums[i+1] + nums[j]);
                }
            }
        }
        return result;
    }
};