class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end());
        stack<vector<int>> intervalStack;
        
        for (const vector<int> &interval : intervals) {
            if (intervalStack.empty()) intervalStack.push(interval);
            else if (intervalStack.top()[1] < interval[0]) {
                intervalStack.push(interval);
            } else {
                vector<int> newInterval{interval[0], max(interval[1], intervalStack.top()[1])};
                while (!intervalStack.empty() && intervalStack.top()[1] >= interval[0]) {
                    newInterval[0] = intervalStack.top()[0];
                    intervalStack.pop();
                }
                intervalStack.push(newInterval);
            }
        }
        
        vector<vector<int>> result (intervalStack.size(), vector<int>{0, 0});
        for (int i = result.size() - 1; i >= 0; --i) {
            result[i] = intervalStack.top();
            intervalStack.pop();
        }

        return result;
    }
};