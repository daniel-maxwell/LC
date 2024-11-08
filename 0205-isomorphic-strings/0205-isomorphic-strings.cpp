auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const bool isIsomorphic(const string s, const string t) {
        map<char, char> sToT;
        map<char, char> tToS;
        for (int i = 0; i < s.size(); ++i) {
            if (sToT.contains(s[i]) && sToT[s[i]] != t[i]) return false;
            if (tToS.contains(t[i]) && tToS[t[i]] != s[i]) return false;
            sToT[s[i]] = t[i];
            tToS[t[i]] = s[i];
        }
        return true;
    }
};