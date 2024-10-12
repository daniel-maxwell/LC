auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> bracketStack;
        unordered_set<int> toRemove;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                bracketStack.push(i);
            } else if (s[i] == ')') {
                if (bracketStack.empty()) {
                    toRemove.insert(i);
                } else {
                    bracketStack.pop();
                }
            }
        }

        while (!bracketStack.empty()) {
            toRemove.insert(bracketStack.top());
            bracketStack.pop();
        }

        string result = "";

        for (int i = 0; i < s.size(); ++i) {
            if (toRemove.contains(i)) continue;
            result += s[i];   
        }

        return result;
    }
};