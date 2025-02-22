class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.size() != goal.size()) return false;
        unordered_set<char> charSet;
        bool containsDuplicates = false;
        char mismatched;
        int mismatches = 0, mismatchedIdx = -1;
        for (int i = 0; i < s.size(); ++i) {
            if (charSet.contains(s[i])) containsDuplicates = true;
            else charSet.insert(s[i]);
            if (s[i] != goal[i]) {
                if (mismatches == 2) return false;
                else if (mismatches == 1) {
                    if (mismatched != goal[i] || s[i] != goal[mismatchedIdx]) {
                        return false;
                    }
                } else {
                    mismatched = s[i];
                    mismatchedIdx = i;
                }
                ++mismatches;
            }
        }
        return mismatches == 2 || (mismatches == 0 && containsDuplicates);
    }
};