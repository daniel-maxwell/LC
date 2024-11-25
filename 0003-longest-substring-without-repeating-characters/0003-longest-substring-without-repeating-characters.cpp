static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int l = 0, r = 0;
        int result = 0;
        while (r < s.size()) {
            while (charSet.contains(s[r])) {
                charSet.erase(s[l]);
                ++l;
            }
            charSet.insert(s[r]);
            ++r;
            result = max(result, r - l);
        }
        return result;
    }
};