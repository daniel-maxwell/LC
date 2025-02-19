class Solution {
public:
    const string shortestCompletingWord(const string licensePlate, const vector<string>& words) {
    
        const unordered_set<char> letters {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        };
        unordered_map<char, int> lpCharCounts;

        int length = 0;

        for (const char &c : licensePlate) {
            if (letters.contains(c)) {
                ++lpCharCounts[tolower(c)];
                if (lpCharCounts[tolower(c)] == 1) {
                    ++length;
                }
            }
        }

        string result = "";

        for (const string &word : words) {
            int matches = 0;
            unordered_map<char, int> charCounts;
            for (const char &c : word) {
                const char character = tolower(c);
                if (lpCharCounts.contains(character)) {
                    ++charCounts[character];
                    if (charCounts[character] == lpCharCounts[character]) {
                        ++matches;
                    }
                }
            }
            if (matches == length) {
                if (result == "" || result.size() > word.size()) {
                    result = word;
                }
            }
        }

        return result;
        
    }
};