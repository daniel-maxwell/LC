class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> charCounts {
                { 'b', 0 },
                { 'a', 0 },
                { 'l', 0 },
                { 'o', 0 },
                { 'n', 0 }
        };

        for (int i = 0; i < text.size(); ++i) {
            if (charCounts.find(text[i]) != charCounts.end()) {
                ++charCounts[text[i]];
            };
        };

        charCounts['l'] = floor(charCounts['l'] / 2);
        charCounts['o'] = floor(charCounts['o'] / 2);

        int result = charCounts['b'];

        for (pair<char, int> entry : charCounts) {
            if (entry.second < result) result = entry.second;
        };
        return result; 
    };
};