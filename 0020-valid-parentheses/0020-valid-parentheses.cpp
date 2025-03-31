class Solution {
public:
    bool isValid(string s) {
    
        unordered_map<char, char> bracketMap {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'} 
        };

        stack<char> bracketStack;

        for (const char &c : s) {
            if (bracketMap.contains(c)) {
                bracketStack.push(c);
            }
            else {
                if (bracketStack.empty()) {
                    return false;
                }
                if (bracketMap[bracketStack.top()] != c) {
                    return false;
                }
                bracketStack.pop();
            }
        }

        return bracketStack.empty();
    }
};