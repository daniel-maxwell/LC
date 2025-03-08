class Solution {
public:
    const vector<vector<int>> indexPairs(const string text, const vector<string>& words) {
        vector<vector<int>> result;
        unordered_set<char> charSet;
        const unordered_set<string> wordSet(words.begin(), words.end());

        for (const string &w : words) {
            for (const char &c : w) {
                charSet.insert(c);
            }
        }

        int i = 0;

        while (i < text.size()) {
            if (charSet.contains(text[i])) {
                int j = i + 1;
                string word(1, text[i]);
                if (wordSet.contains(word)) {
                    result.push_back(vector<int>{i, i});
                }
                while (j < text.size() && charSet.contains(text[j])) {
                    cout << word << endl;
                    word += text[j];
                    if (wordSet.contains(word)) {
                        result.push_back(vector<int>{i, j});
                    }
                    ++j;
                }
            }
            ++i;
        }
        
        return result;
    }
};