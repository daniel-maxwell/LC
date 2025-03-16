class Solution {
public:
    const int ladderLength(const string beginWord, const string endWord, const vector<string>& wordList) {
        
        unordered_set<string> visited;
        queue<string> q;
        q.push(beginWord);
        int depth = 1;

        while (!q.empty() && depth <= wordList.size()) {
            int length = q.size();
            for (int i = 0; i < length; ++i) {
                const string curWord = q.front();
                q.pop();
                for (const string &word : wordList) {
                    if (visited.contains(word)) continue;
                    if (differsByOneLetter(curWord, word)) {
                        if (word == endWord) {
                            return depth + 1;
                        }
                        q.push(word);
                        visited.insert(word);
                    }
                }
            }
            ++depth;
        }

        return 0;

    }

    const bool differsByOneLetter(const string &word1, const string &word2) {
        bool foundDifference = false;
        for (int i = 0; i < word1.size(); ++i) {
            if (word1[i] != word2[i]) {
                if (foundDifference) {
                    return false;
                }
                foundDifference = true;
            }
        }
        return true;
    }
};