class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        map<char, int> charCounts;
        for (const char c : chars) {
            ++charCounts[c];
        }
        int result = 0;
        for (const string word : words) {
            map<char, int> wordCharCounts;
            bool canFormWord = true;
            for (const char c : word) {
                if (!charCounts.contains(c)) {
                    canFormWord = false;
                    break;
                }
                ++wordCharCounts[c];
                if (wordCharCounts[c] > charCounts[c]) {
                    canFormWord = false;
                    break;
                }
            }
            if (canFormWord) result += word.size();
        }
        return result;
    }
};