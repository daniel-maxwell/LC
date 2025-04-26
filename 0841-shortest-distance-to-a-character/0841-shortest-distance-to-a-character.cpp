class Solution {
public:
    const vector<int> shortestToChar(const string s, const char c) {

        vector<int> shortestRight (s.size(), 0);
        vector<int> result (s.size(), 0);
        
        int dist = -1;
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == c) dist = 0;
            shortestRight[i] = dist;
            if (dist != -1) ++dist;
        }

        dist = -1;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == c) dist = 0;
            if (dist == -1) {
                result[i] = shortestRight[i];
            } else if (shortestRight[i] == -1) {
                result[i] = dist;
            } else {
                result[i] = min(dist, shortestRight[i]);
            }
            
            if (dist != -1) ++dist;
        }

        return result;
    }
};