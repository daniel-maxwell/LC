static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    inline void rtrim(std::string &s) {
        s.erase(std::find_if(s.rbegin(), s.rend(), [](unsigned char ch) {
            return !std::isspace(ch);
        }).base(), s.end());
    }
    inline void trim(std::string &s) { rtrim(s); }
    int lengthOfLastWord(string s) {
        rtrim(s);
        string stringStore;
        stringstream ss(s);
        string prev;
        while (getline(ss, s, ' ')) prev = s;
        return prev.size();
    }
};