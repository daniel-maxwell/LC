class Solution {
public:
    const string reverseVowels(string s) {
        const unordered_set<char> vowels {
            'A', 'E', 'I', 'O', 'U', 
            'a', 'e', 'i', 'o', 'u'
        };
        int l = 0, r = s.size() - 1;
        while (l < r) {
            while (!vowels.contains(s[l])) {
                ++l;
                if (l == r) return s;
            }
            while (!vowels.contains(s[r])) {
                --r;
                if (l == r) return s;
            }
            const char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            ++l;
            --r;
        }
        return s;
    }
};