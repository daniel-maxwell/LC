class Solution {
public:
    string removeDuplicates(string s) {

        stack<char> charStack;

        for (const char &c : s) {
            if (!charStack.empty() && charStack.top() == c) {
                charStack.pop();
            } else {
                charStack.push(c);
            }
        }

        string result = "";

        while (!charStack.empty()) {
            result += charStack.top();
            charStack.pop();
        }

        reverse(result.begin(), result.end());

        return result;
    }
};