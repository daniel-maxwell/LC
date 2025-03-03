class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums.front();
        }
        int result = max(nums[0], nums[1]);
        int maxPrev = nums[0];      
        for (int i = 2; i < nums.size(); ++i) {
            int temp = max(maxPrev + nums[i], result);
            maxPrev = result;
            result = temp;
        }
        return result;
    }
};