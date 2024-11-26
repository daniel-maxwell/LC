static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int l = 0, r = 0;
        int result = 0;
        int curK = k;
        while (r < nums.size()) {
            if (r < nums.size() - 1 && nums[r + 1] == nums[r]) {
                ++r;
            } else if (curK == 0 || l == -1 || curK < nums[r] - nums[l]) {
                result = max(r - l, result);
                ++r;
                l = r;
                curK = k;
                continue;
            } else {
                curK -= nums[r] - nums[l];
                --l;
            }
        }
        return result;
    }
};