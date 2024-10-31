auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> sMap;
        map<char, int> tMap;
        for (const char& sChar : s) ++sMap[sChar];
        for (const char& tChar : t) ++tMap[tChar];
        return sMap == tMap;
    }
};