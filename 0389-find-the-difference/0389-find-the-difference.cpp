class Solution {
public:
    const char findTheDifference(const string s, const string t) {
        unordered_map<char, int> sMap;
        for (const char& c : s) ++sMap[c];
        for (const char& c : t) {
            if (!sMap.contains(c)) return c;
            --sMap[c];
            if (sMap[c] == 0) sMap.erase(c);
        }
        return 'a';
    }
};