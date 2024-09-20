static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1;
        int b = 2;
        n -= 2;
        while (n > 0) {
            int temp = a + b;
            a = b;
            b = temp;
            --n;
        }
        return b;
    }
};