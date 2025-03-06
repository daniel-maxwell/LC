class Solution {
public:
    int fib(int n) {
        int result = n == 0 ? 0 : 1;
        int prev = 0;
        for (int i = 2; i <= n; ++i) {
            int temp = result + prev;
            prev = result;
            result = temp;
        }
        return result;
    }
};