class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.length() == 0) return true;
        int matchedChars = 0;
        for (int i = 0; i < t.size(); ++i) { 
            if (matchedChars < s.size() && s[matchedChars] == t[i]) matchedChars++;
        }
        return matchedChars == s.size();
    }
};