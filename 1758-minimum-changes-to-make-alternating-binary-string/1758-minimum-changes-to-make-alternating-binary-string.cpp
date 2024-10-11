auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    int minOperations(string s) {
        int diffStartingWith0 = 0;
        int diffStartingWith1 = 0;
        bool startingWith0 = false;
        for (const char& c : s) {
            if ((c == '0') == startingWith0) {
                ++diffStartingWith1;
            } else {
                ++diffStartingWith0;
            }
            startingWith0 = !startingWith0;
        }
        return min(diffStartingWith1, diffStartingWith0);
    }
};