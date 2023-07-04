class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int length;
        if (word1.size() <= word2.size()) length = word1.size() + 1;
        else length = word2.size() + 1;
        vector<char>output(word1.size() + word2.size());
        for (int i = 0; i < length; ++i) {
            if (i == word1.size() || i == word2.size()) {
                if (word1.size() == word2.size()) {
                    string str{ output.begin(), output.end() };
                    return str;
                }
                else if (word1.size() > word2.size()) {
                    for (int j = i*2; j < output.size(); ++j) {
                        output[j] = word1[i];
                        ++i;
                    };
                    string str{ output.begin(), output.end() };
                    return str;
                }
                else {
                    for (int j = i*2; j < output.size(); ++j) {
                        output[j] = word2[i];
                        ++i;
                    };
                    string str{ output.begin(), output.end() };
                    return str;
                };
            };
            output[i + i] = word1[i];
            output[i + i + 1] = word2[i];
        };
        return "fail";
    };
};