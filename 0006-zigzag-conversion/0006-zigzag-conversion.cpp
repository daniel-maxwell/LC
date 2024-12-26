class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        vector<int> intervals;
        int curr = numRows - 2;
        for (int i = 0; i < numRows - 1; ++i) {
            intervals.push_back(numRows + curr);
            curr -= 2;
        }
        intervals.push_back(intervals[0]);

        string result = "";
        int interval = 0;

        while (interval < numRows) {
            int first = intervals[interval];
            int second = intervals[intervals.size() - 1 - interval];
            int j = interval;
            while (j < s.size()) {
                result += s[j];
                j += first;
                if (j < s.size()) {
                    result += s[j];
                    j += second;
                }
            }
            ++interval;
        }
        return result;
    }
};