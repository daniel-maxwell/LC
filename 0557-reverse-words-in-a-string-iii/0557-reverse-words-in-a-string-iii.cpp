class Solution {
public:
    string reverseWords(string s) {
        vector<int> spaces;
        vector<string> words;

        int wordCount = 0;

        string word = "";
        string result = "";

        for (size_t i = 0; i < s.size(); ++i) {
            if (s[i] == ' ') {
                spaces.push_back(i);
                if (i > 0 && s[i-1] != ' ') { // Check for previous character
                    reverse(word.begin(), word.end());
                    words.push_back(word);
                    word = "";
                }
            } else {
                if (i > 0 && s[i-1] == ' ') { // Check for previous character
                    ++wordCount;
                }
                word += s[i];
            }
        }

        // Process the last word
        if (!word.empty()) {
            reverse(word.begin(), word.end());
            words.push_back(word);
        }

        size_t i = 0;
        size_t j = 0;
        size_t k = 0;
        while (i < words.size()) {
            if (j < spaces.size() && k == spaces[j]) {
                result += ' ';
                ++j;
                ++k;
            } else {
                result += words[i];
                k += words[i].size();
                ++i;
            }
        }
        while (j < spaces.size()) {
            result += ' ';
            ++j;
        }

        return result;
    }
};