class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
            unordered_set<string> oneOccurence;
            unordered_set<string> twoOrMore;
            string window = "";
            int l = 0, r = 9;

            while (r < s.size()) {
                for (int i = l; i <= r; ++i) {
                    window.push_back(s[i]);
                }
                if (oneOccurence.count(window)) {
                    twoOrMore.insert(window);
                }
                else {
                    oneOccurence.insert(window);
                }
                ++l;
                ++r;
                window = "";
            }
            const vector<string> output(twoOrMore.begin(), twoOrMore.end());
            return output;
    }
};