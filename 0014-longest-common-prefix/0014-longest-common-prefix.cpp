class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        int charPtr = 0;
        char curChar;
        string result = "";
        bool foundResult = false;

        while (!foundResult) {
            if (charPtr == strs[0].size()) {
                foundResult = true;
                break;
            }
            char curChar = strs[0][charPtr];
            for (const string &s : strs) {
                if (charPtr == s.size() || s[charPtr] != curChar) {
                    foundResult = true;
                    break;
                }
            }
            if (!foundResult) {
                result += curChar;
                ++charPtr;
            } 
        }
        
        return result;
    }
};