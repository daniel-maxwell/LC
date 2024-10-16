auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0)
            return false;
        if (n > 1 && n % 4 == 0) {
            return isPowerOfFour(n / 4);
        } else if (n > 1 && (n % 4) != 0) {
            return false;
        }
        return true;
    }
};