class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> mapST, mapTS;
        for (int i = 0; i < s.size(); ++i) {
            if ((mapST.find(s[i]) != mapST.end() && mapST.at(s[i]) != t[i]) ||
                (mapTS.find(t[i]) != mapTS.end() && mapTS.at(t[i]) != s[i])) {
                return false;
            }
            mapST.insert_or_assign(s[i], t[i]);
            mapTS.insert_or_assign(t[i], s[i]);
        };
        return true;
    };
};