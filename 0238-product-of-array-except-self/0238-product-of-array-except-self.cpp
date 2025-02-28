class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix = 1;
        vector<int> result (nums.size(), 0);
        
        for (int i = nums.size() - 1; i >= 0; --i) {
            if (i < nums.size() - 1) {
                result[i] = nums[i] * result[i + 1];
            } else {
                result[i] = nums[i];
            }
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (i < nums.size() - 1) {
                result[i] = prefix * result[i + 1];
            } else {
                result[i] = prefix;
            }
            prefix *= nums[i];
        }

        return result;
    }
};