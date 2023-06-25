class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0, j = s.size() - 1;
        int baseCase = s.size() % 2;
        while ((j - i) > baseCase) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            ++i;
            --j;
        };
    };
};