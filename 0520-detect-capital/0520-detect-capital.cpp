class Solution {
public:
    bool detectCapitalUse(const string word) {
        const unordered_set<char> capitals {
            'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z'
        };

        vector<int> capitalIndices;

        for (int i = 0; i < word.size(); ++i) {
            if (capitals.contains(word[i])) {
                capitalIndices.push_back(i);
            }
        }

        return capitalIndices.empty() || 
               capitalIndices.size() == word.size() || 
               capitalIndices.back() == 0;
    }
};