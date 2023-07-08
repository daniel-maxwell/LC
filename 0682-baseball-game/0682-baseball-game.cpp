class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> stack = {};
        int sum = 0;
        for (string s : operations) {
            if (s == "+") {
                int val = stack[stack.size() - 2] + stack[stack.size() - 1];
                sum += val;
                stack.push_back(val);
            }
            else if (s == "D") {
                int val = stack[stack.size() - 1] * 2;
                sum += val;
                stack.push_back(val);
            }
            else if (s == "C") {
                sum -= stack[stack.size() - 1];
                stack.pop_back();
            }
            else {
                int val = stoi(s);
                sum += val;
                stack.push_back(val);
            };
        };
        return sum;
    };
};