class Solution {
public:
    const vector<vector<int>> findMissingRanges(const vector<int>& nums, int lower, int upper) {
        
        if (nums.empty()) return vector<vector<int>>{{lower, upper}};

        vector<vector<int>> result;

        if (lower < nums[0]) {
            result.push_back(vector<int>{lower, nums[0] - 1});
        }

        int i = 0;

        while (i < nums.size() - 1) {
            if (nums[i + 1] - nums[i] > 1) {
                result.push_back(vector<int>{nums[i] + 1, nums[i + 1] - 1});
            }
            ++i;
        }

        if (nums.back() < upper) {
            result.push_back(vector<int>{nums.back() + 1, upper});
        }

        return result;
    }
};