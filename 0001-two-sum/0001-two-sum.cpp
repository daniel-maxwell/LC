static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    vector<int> twoSum(const vector<int>& nums, const int target) {
        map<int, int>numsToIdx;
        for (int i = 0; i < nums.size(); ++i) {
            if (numsToIdx.contains(target - nums[i])) return vector<int> {numsToIdx.at(target - nums[i]), i};
            numsToIdx[nums[i]] = i;
        }
        return nums;
    }
};