class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {

        vector<int> furthestLeft {0};

        int l = 0;
        int r = 1;

        int furthestBack = -1;

        while (r < nums.size()) {
            while (nums[r] - nums[l] > maxDiff) {
                ++l;
            }
            if (l == r) furthestBack = l;
            furthestLeft.push_back(furthestBack);
            ++r;
        }

        vector<bool>result;

        for (const vector<int> &query : queries) {

            if (nums[query[0]] < nums[query[1]]) {
                result.push_back(furthestLeft[query[1]] <= query[0]);

            } else if (nums[query[0]] > nums[query[1]]) {
                result.push_back(furthestLeft[query[0]] <= query[1]);
            } else {
                result.push_back(true);
            }
        }

        return result;
        
    }
};