class Solution {
public:
    const string removeVowels(const string &s) {
        const unordered_set<char> vowels {
            'a', 'e', 'i', 'o', 'u'
        };
        string result = "";
        for (const char &c : s) {
            if (vowels.contains(c)) {
                continue;
            }
            result += c;
        }
        return result;
    }
};