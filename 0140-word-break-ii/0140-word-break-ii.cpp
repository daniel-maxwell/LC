class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        wordSet = unordered_set<string>(wordDict.begin(), wordDict.end());
        str = s;
        backtrack("", "", 0);
        return result;
    }

private:
    void backtrack(string curSentence, string curWord, const int i) {
        if (i == str.size()) { // Base Case
            if (wordSet.contains(curWord)) {
                curSentence += curSentence.size() > 0 ? " " + curWord : curWord;
                curWord = "";
            }
            if (curWord.size() == 0) {
                result.push_back(curSentence);
            }
            return;
        }
        if (curWord.size() == 0 || !wordSet.contains(curWord)) {
            curWord += str[i];
            backtrack(curSentence, curWord, i + 1);
        } else {
            backtrack(curSentence, curWord + str[i], i + 1); // ignore
            curSentence += curSentence.size() > 0 ? " " + curWord : curWord;
            curWord = "";
            backtrack(curSentence, curWord, i);
        }
        return;
    }
    unordered_set<string> wordSet;
    string str;
    vector<string> result {};
};