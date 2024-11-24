static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    const int jump(const vector<int>& nums) {
        int result = 0;
        int l = 0, r = 0;
        while (r < nums.size() - 1) {
            int furthestJump = 0;
            for (int i = l; i <= r; ++i) {
                furthestJump = max(furthestJump, i + nums[i]);
            }
            l = r + 1;
            r = furthestJump;
            ++result;
        }
        return result;
    }
};