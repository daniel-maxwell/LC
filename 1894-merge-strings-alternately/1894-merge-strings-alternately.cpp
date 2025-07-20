class Solution {
public:
    const string mergeAlternately(const string &word1, const string &word2) {
        string s;
        s.reserve(word1.size() + word2.size());
        size_t i = 0;
        while (i < word1.size() || i < word2.size()) {
            if (i < word1.size()) s += word1[i];
            else {
                s += word2.substr(i, word2.size() - i);
                break;
            }
            if (i < word2.size()) s += word2[i];
            else {
                s += word1.substr(i + 1, word1.size() - i);
                break;
            }
            ++i;
        }
        return s;
    }
};