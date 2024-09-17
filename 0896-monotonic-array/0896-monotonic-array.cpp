int speedUp = [] {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    return 0;
}();
 
class Solution {
    public:
    bool isMonotonic(const vector<int>& nums) {
        int prev = nums[0];
        int dir = 0;
        for (const int el : nums) {
            if (el > prev) {
                if (dir == -1) return false;
                dir = 1;
        } else if (el < prev) {
            if (dir == 1) return false;
            dir = -1;
        }
        prev = el;
        }
        return true;
    }
};