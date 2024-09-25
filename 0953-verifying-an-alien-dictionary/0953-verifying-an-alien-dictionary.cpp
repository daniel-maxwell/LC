static const bool Booster = [](){
    ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    bool isAlienSorted(vector<string>& words, const string order) {
        map<char, int> orderMap;
        int idx = 1;
        for (const char c : order) {
            orderMap[c] = idx;
            ++idx;
        }
        for (int i = 0; i < words.size() - 1; ++i) {
            string wordA = words[i];
            string wordB = words[i+1];
            int j = 0;
            bool substr = true;
            while (j < wordA.size() && j < wordB.size()) {
                if (orderMap[wordA[j]] < orderMap[wordB[j]]) {
                    substr = false;
                    break;
                }
                if (orderMap[wordA[j]] > orderMap[wordB[j]]) return false;
                if (substr && wordA[j] != wordB[j]) substr = false;
                ++j;
            }
            if (substr && wordA.size() > wordB.size()) return false;
        }
        return true;
    }
};;