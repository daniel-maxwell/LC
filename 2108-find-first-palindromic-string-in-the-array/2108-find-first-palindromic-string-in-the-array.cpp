auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const string firstPalindrome(const vector<string>& words) {
        for (const string &word : words) {
            if (isPalindrome(word)) {
                return word;
            }
        }
        return "";
    }
    const bool isPalindrome(const string &str) {
        size_t l = 0, r = str.size() - 1;
        while (l < r) {
            if (str[l] != str[r]) {
                return false;
            }
            ++l;
            --r;
        }
        return true;
    }
};