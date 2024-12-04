class Solution {
public:
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        
        vector<int> platesPerIndex;
        vector<int> nearestCandleLeft;
        vector<int> nearestCandleRight(s.size(), -1);

        int i = 0, platesCounter = 0, lastCandleIdx = -1;

        while (i < s.size() && s[i] != '|') {
            platesPerIndex.push_back(0);
            nearestCandleLeft.push_back(lastCandleIdx);
            ++i;
        }

        while (i < s.size()) {
            if (s[i] == '*') {
                ++platesCounter;
            } else {
                lastCandleIdx = i;
            }
            platesPerIndex.push_back(platesCounter);
            nearestCandleLeft.push_back(lastCandleIdx);
            ++i;
        }

        lastCandleIdx = -1;
        i = s.size() - 1;

        while (i >= 0) {
            if (s[i] == '|') {
                lastCandleIdx = i;
            }
            nearestCandleRight[i] = lastCandleIdx;
            --i;
        }

        vector<int> result;
        for (const vector<int> &query : queries) {
            int l = nearestCandleRight[query[0]];
            int r = nearestCandleLeft[query[1]];
            if (l >= r || l < 0 || r < 0) result.push_back(0);
            else result.push_back(platesPerIndex[r] - platesPerIndex[l]);
        }

        return result;        
    }
};