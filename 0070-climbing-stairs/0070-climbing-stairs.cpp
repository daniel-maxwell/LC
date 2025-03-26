class Solution {
public:
    int climbStairs(int n) {
        int a = 1;
        int b = 2;
        for (int i = 2; i < n; ++i) {
            const int temp = a + b;
            a = b;
            b = temp;
        }
        return n == 1 ? a : b;
    }
};