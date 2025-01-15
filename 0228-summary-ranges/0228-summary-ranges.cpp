class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = 0, r = 1;
        vector<string> result;
        while (l < nums.size()) {
            while (r < nums.size() && nums[r] == nums[r-1] + 1) {
                ++r;
            }
            if (r - l == 1) {
                result.push_back(to_string(nums[r-1]));
            } else {
                result.push_back(to_string(nums[l]) + "->" + to_string(nums[r-1]));
            }
            l = r;
            ++r;
        }
        return result;
    }
};