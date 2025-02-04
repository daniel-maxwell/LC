class Solution {
public:
    const char nextGreatestLetter(const vector<char>& letters, const char target) {
        const int targetNum = target - 'a';
        for (const char &letter : letters)
            if (letter - 'a' > targetNum) return letter;
        return letters[0];
    }
};