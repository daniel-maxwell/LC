class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<char> x (s.begin(), s.end());
        vector<char> y (t.begin(), t.end());
        std::sort(x.begin(), x.end());
        std::sort(y.begin(), y.end());
        string a (x.begin(), x.end());
        string b (y.begin(), y.end());
        return a == b;
    }
};