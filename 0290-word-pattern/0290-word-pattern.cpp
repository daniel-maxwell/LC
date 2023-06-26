class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words {};
        size_t pos = 0;
        while ((pos = s.find(" ")) != string::npos) {
            words.push_back(s.substr(0, pos));
            s.erase(0, pos + 1);
        }
        words.push_back(s);
        if (pattern.size() != words.size()) return false;

        unordered_map <char, string> ptnToWord {};
        unordered_map <string, char> wordToPtn {};

        for (int i = 0; i < pattern.size(); ++i) {
            if (ptnToWord.find(pattern[i]) != ptnToWord.end() &&
                ptnToWord[pattern[i]] != words[i]) return false;

            if (wordToPtn.find(words[i]) != wordToPtn.end() &&
                wordToPtn[words[i]] != pattern[i]) return false;

            ptnToWord.insert(std::make_pair(pattern[i], words[i]));
            wordToPtn.insert(std::make_pair(words[i], pattern[i]));
        }
        return true;
    };
};