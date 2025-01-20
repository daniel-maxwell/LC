class Solution {
public:
    const int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        const int length = nums.size();
        return max(nums[0] * nums[1] * nums.back(), nums.back() * nums[length-2] * nums[length-3]);
    }
};