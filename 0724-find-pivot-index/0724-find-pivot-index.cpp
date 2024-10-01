static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sumRight = 0, sumLeft = 0;
        for (const int num : nums) sumRight += num;
        for (int i = 0; i < nums.size(); ++i) {
            sumRight -= nums[i];
            if (sumLeft == sumRight) return i;
            sumLeft += nums[i];
        }
        return -1;
    }
};