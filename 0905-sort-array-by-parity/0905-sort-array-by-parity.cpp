class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int l = 0;
        while (l < nums.size()) {
            if (nums[l] % 2 == 0) {
                ++l;
                continue;
            }
            int r = l + 1;
            while (r < nums.size() && nums[r] % 2 == 1) ++r;
            if (r == nums.size()) return nums;
            swap(nums.at(l), nums.at(r));
            ++l;
        }
        return nums;
    }
};