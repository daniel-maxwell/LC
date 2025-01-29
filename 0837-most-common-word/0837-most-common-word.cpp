class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {

        const unordered_set<string>bannedSet(banned.begin(), banned.end());

        unordered_map<string, int> wordCounts {
            {"/", -1}
        };

        const unordered_set<char> letters {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
            'U', 'V', 'W', 'X', 'Y', 'Z'
        };

        int i = 0;

        string buffer = "", result = "/";

        while (i < paragraph.size()) {
            while (i < paragraph.size() && letters.contains(paragraph[i])) {
                buffer += tolower(paragraph[i]);
                ++i;
            }
            if (buffer.size() > 0 && !bannedSet.contains(buffer)) {
                ++wordCounts[buffer];
                if (wordCounts[result] < wordCounts[buffer]) {
                    result = buffer;
                }
            }
            buffer = "";
            ++i;
        }

        return result;
    }
};