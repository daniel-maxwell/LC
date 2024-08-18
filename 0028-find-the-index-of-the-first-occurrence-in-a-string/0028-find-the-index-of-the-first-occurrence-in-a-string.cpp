class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t idx = haystack.find(needle);
        int res = (idx == string::npos) ? -1 : static_cast<int>(idx);
        return res;
    }
};