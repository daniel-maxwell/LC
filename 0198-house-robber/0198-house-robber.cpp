class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() >= 2) nums[1] = max(nums[0], nums[1]);
        else return nums.back();
        for (int i = 2; i < nums.size(); ++i) {
            nums[i] = max(nums[i-2] + nums[i], nums[i-1]);
        }
        return nums.back();
    }
};