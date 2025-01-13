class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> visited {beginWord};
        queue<string> q; 
        q.push(beginWord);
        int result = 1;

        while (!q.empty()) {
            const int length = q.size();
            for (int _ = 0; _ < length; ++_) {
                const string cur = q.front();
                if (cur == endWord) return result;
                q.pop();
                for (const string &word : wordList) {
                    if (visited.contains(word)) continue;
                    if (canTraverse(cur, word)) {
                        visited.insert(word);
                        q.push(word);
                    }
                }
            }
            ++result;
        }
        return 0;
    }

private:
    const bool canTraverse(const string &s, const string &t) {
        bool differs = false;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != t[i]) {
                if (differs) return false;
                differs = true;
            }
        }
        return true;
    }
};
