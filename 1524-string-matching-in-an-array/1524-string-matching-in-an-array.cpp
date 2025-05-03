class Solution {
public:
    const vector<string> stringMatching(vector<string>& words) {
        sort(words.begin(), words.end());
        vector<string> result;
        for (int i = 0; i < words.size(); ++i) {
            for (int j = 0; j < words.size(); ++j) {
                if (words[i].size() >= words[j].size() ||
                    i == j) continue;
                if (isSubstr(words[i], words[j])) {
                    result.push_back(words[i]);
                    break;
                }
            }
        }
        return result;
    }

    const bool isSubstr(const string &wordA, const string &wordB) {
        int l = 0, r = wordA.size();
        while (r <= wordB.size()) {
            if (wordA == wordB.substr(l, r - l)) {
                return true;
            }
            ++l;
            ++r;
        }
        return false;
    }
};