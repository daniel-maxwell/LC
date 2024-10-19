auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const bool arrayStringsAreEqual(const vector<string>& word1, const vector<string>& word2) {
        std::ostringstream oss1, oss2;
        for (const string& el : word1) {
            oss1 << el;
        }
        for (const string& el : word2) {
            oss2 << el;
        }
        return oss1.str() == oss2.str();
    }
};