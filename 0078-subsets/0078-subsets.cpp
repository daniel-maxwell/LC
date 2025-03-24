class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        numsCopy = nums;
        vector<int> cur;
        backtrack(0, cur);
        return result;
    }

    void backtrack(int i, vector<int>& cur) {
        if (i == numsCopy.size()) {
            result.push_back(cur);
            return;
        }
        cur.push_back(numsCopy[i]);
        backtrack(i + 1, cur);
        cur.pop_back();
        backtrack(i + 1, cur);
    }
    vector<int> numsCopy;
    vector<vector<int>> result;
};