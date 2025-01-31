class Solution {
public:
    const int shortestDistance(const vector<string>& wordsDict, const string word1, const string word2) {
        
        int result = wordsDict.size();
        vector<int> w1Indices;
        vector<int> w2Indices;

        for (int i = 0; i < wordsDict.size(); ++i) {
            if (wordsDict[i] == word1) {
                w1Indices.push_back(i);
                if (!w2Indices.empty()) {
                    result = min(i - w2Indices.back(), result);
                }

            }
            if (wordsDict[i] == word2) {
                w2Indices.push_back(i);
                if (!w1Indices.empty()) {
                    result = min(i - w1Indices.back(), result);
                }

            }
        }

        return result;    
    }
};