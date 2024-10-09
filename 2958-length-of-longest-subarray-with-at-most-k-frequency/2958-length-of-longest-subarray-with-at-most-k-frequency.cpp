static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    const int maxSubarrayLength(const vector<int>& nums, const int k) {
        int l = 0, r = 0;
        int result = 0;
        int currMaxFreq = 1;
        map<int, int> freqs;
        while (r < nums.size()) {
            ++freqs[nums[r]];
            currMaxFreq = max(currMaxFreq, freqs[nums[r]]);
            while (freqs[nums[r]] > k) {
                --freqs[nums[l]];
                ++l;
            }
            result = max(result, r - l + 1);
            ++r;
        }
        return result;
    }
};