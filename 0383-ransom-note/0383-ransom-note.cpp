class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int length = ransomNote.size();

        unordered_map<char, int> charCounts;

        for (const char &c : ransomNote) {
            ++charCounts[c];
        }

        for (const char &c : magazine) {
            if (charCounts.contains(c) && charCounts[c] > 0) {
                --length;
                --charCounts[c];
                if (length == 0) return true;
            }
        }
        
        return false;
    }
};