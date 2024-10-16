auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n < 0) return false;
        for(int i = 0; i < 31; ++i){
            if (n == pow(4, i)) {
                return true;
            }
        }
        return false;
    }
};