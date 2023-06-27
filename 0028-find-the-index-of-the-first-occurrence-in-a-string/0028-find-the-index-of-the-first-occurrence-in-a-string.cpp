class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.size() <= needle.size()) {
                if (needle.compare(haystack) == 0) return 0;
                else return -1;
            }
            else {
                for (int i = 0; i < haystack.size() - needle.size() +1; ++i) {
                    string substr = haystack.substr(i, needle.size());
                    if (substr.compare(needle) == 0) return i;
                }
            }
            return -1;
    }
};