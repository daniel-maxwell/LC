class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";

        int w1Ptr = 0;
        int w2Ptr = 0;

        while (w1Ptr < word1.size() || w2Ptr < word2.size()) {
            if (w1Ptr < word1.size()) result += word1[w1Ptr];
            if (w2Ptr < word2.size()) result += word2[w2Ptr];
            ++w1Ptr;
            ++w2Ptr;
        }

        return result;
    }
};