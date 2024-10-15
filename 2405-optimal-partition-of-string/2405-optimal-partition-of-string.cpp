auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    int partitionString(string s) {
        set<char> charSet;
        int result = 1;
        for (const char &c : s) {
            if (charSet.contains(c)) {
                ++result;
                charSet.clear();
            }
            charSet.insert(c);
        }
        return result;
    }
};