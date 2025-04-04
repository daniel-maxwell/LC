static const bool init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return true;
}();
class Solution {
public:
    const bool isPalindrome(const int x) {
        const string strX = to_string(x);
        int l = 0, r = strX.size() - 1;
        while (l < r) {
            if (strX[l] != strX[r]) return false;
            ++l;
            --r;
        }
        return true;
    }
};