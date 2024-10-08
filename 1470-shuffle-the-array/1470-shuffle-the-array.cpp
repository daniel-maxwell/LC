static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> result;
        for (int i = 0; i < nums.size() / 2; ++i) {
            const int j = i + (nums.size() / 2);
            result.push_back(nums[i]);
            result.push_back(nums[j]);
        }
        return result;
    }
};