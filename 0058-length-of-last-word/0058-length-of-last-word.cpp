static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int lengthOfLastWord(string s) {
        s.erase(s.find_last_not_of(" \n\r\t") + 1);
        if (s.size() == 1) return 1;
        int finalDelimIndex = -1;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ' ') finalDelimIndex = i;
        }
        return s.substr(finalDelimIndex+1, string::npos).size();
    }
};