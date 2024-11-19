static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = nums[0], currSum = 0;
        for (const int &n : nums) {
            currSum = currSum < 0 ? 0 : currSum;
            currSum += n;
            result = max(result, currSum);
        }
        return result;
    }
};