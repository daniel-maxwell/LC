class Solution {
public:
    const string toLowerCase(string s) {
        const unordered_map<char, char> lowerMap {
            {'A', 'a'},
            {'B', 'b'},
            {'C', 'c'},
            {'D', 'd'},
            {'E', 'e'},
            {'F', 'f'},
            {'G', 'g'},
            {'H', 'h'},
            {'I', 'i'},
            {'J', 'j'},
            {'K', 'k'},
            {'L', 'l'},
            {'M', 'm'},
            {'N', 'n'},
            {'O', 'o'},
            {'P', 'p'},
            {'Q', 'q'},
            {'R', 'r'},
            {'S', 's'},
            {'T', 't'},
            {'U', 'u'},
            {'V', 'v'},
            {'W', 'w'},
            {'X', 'x'},
            {'Y', 'y'},
            {'Z', 'z'}
        };
        for (int i = 0; i < s.size(); ++i) {
            s[i] = lowerMap.contains(s[i]) ? lowerMap.at(s[i]) : s[i];
        }
        return s;
    }
};