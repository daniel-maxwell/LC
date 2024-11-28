static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    const int maxVowels(const string s, const int k) {
        unordered_set<char> vowelSet {'a', 'e', 'i', 'o', 'u'};
        int vowelCount = 0;
        for (int i = 0; i < k && i < s.size(); ++i) {
            if (vowelSet.contains(s[i])) ++vowelCount;
        }
        int l = 0, r = k, result = vowelCount;
        while (r < s.size()) {
            if (vowelSet.contains(s[l])) --vowelCount;
            if (vowelSet.contains(s[r])) ++vowelCount;
            result = max(result, vowelCount);
            ++l;
            ++r;
        }
        return result;
    }
};