class Solution {
public:
    int minimumOperations(vector<int>& nums) {

        vector<long> longNums;

        for (const int & n : nums) {
            longNums.push_back(static_cast<long>(n));
        }
        int numOperations = 0;
        int i = 0, j = nums.size() - 1;
        while (i < j) {
            if (longNums[i] == longNums[j]) {
                ++i;
                --j;
                continue;
            }
            if (longNums[i] < longNums[j]) {
                longNums[i+1] += longNums[i];
                ++i;
            } else {
                longNums[j-1] += longNums[j];
                --j;
            }
            ++numOperations;
        }
        return numOperations;
    }
};