class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int prev = nums[0];
        int len = 0;
        int maxLen = 0;
        for (const int &n : nums) {
            if (prev >= n) {
                maxLen = max(len, maxLen);
                len = 1;
            } else {
                ++len;
            }
            prev = n;
        }
        return max(len, maxLen);
    }
};