class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int rightSide = accumulate(nums.begin(), nums.end(), 0) - nums[0];
        int leftSide = 0;
        vector<int> result(nums.size(), 0);
        for (int i = 0; i < nums.size(); ++i) {
            int lDiff = (nums[i] * i) - leftSide;
            int rDiff = rightSide - (nums[i] * (nums.size() - i - 1));
            result[i] = lDiff + rDiff;
            leftSide += nums[i];
            rightSide -= i < nums.size() - 1 ? nums[i+1] : 0;
        }
        return result;
    }
};