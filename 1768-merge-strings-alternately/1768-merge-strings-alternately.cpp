auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const string mergeAlternately(const string word1, const string word2) {
        int i = 0;
        string result;
        while (i < word1.size() || i < word2.size()) {
            if (i < word1.size()) {
                result += word1[i];
            }
            if (i < word2.size()) {
                result += word2[i];
            }
            ++i;
        }
        return result;
    }
};