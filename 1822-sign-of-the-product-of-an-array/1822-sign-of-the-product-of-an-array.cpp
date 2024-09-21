#pragma once
static const bool _ = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int arraySign(const vector<int>& nums) {
        bool neg = false;
        for (const int n : nums) {
            if (n == 0) return 0;
            if (n < 0) neg = !neg;
        }
        return neg ? -1 : 1;
    }
};