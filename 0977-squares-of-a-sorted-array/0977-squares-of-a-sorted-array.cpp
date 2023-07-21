class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size(), 0);
        int l = 0, r = nums.size() - 1, x = r;
        while (l <= r) {
            if (pow(nums[l], 2) > pow(nums[r], 2)) {
                res[x] = pow(nums[l], 2);
                ++l;
            }
            else {
                res[x] = pow(nums[r], 2);
                --r;
            }
            --x;
        };
        return res;
    };
};