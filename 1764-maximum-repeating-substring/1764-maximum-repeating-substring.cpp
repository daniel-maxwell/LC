class Solution {
public:
    int maxRepeating(string sequence, string word) {

        if (word.size() > sequence.size()) return 0;

        vector<int> substrIndices;

        for (int i = 0; i <= sequence.size() - word.size(); ++i) {
            if (sequence.substr(i, word.size()) == word) {
                substrIndices.push_back(i);
            }
        }
        
        int result = 0;

        vector<int> ways(sequence.size(), 0);

        while (!substrIndices.empty()) {
            const int curIdx = substrIndices.back();
            substrIndices.pop_back();
            ways[curIdx] = curIdx + word.size() < ways.size() ? 
                           ways[curIdx + word.size()] + 1 : 1;
            result = max(ways[curIdx], result);
        }

        return result;        
    }
};