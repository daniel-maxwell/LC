class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i) {
            int numIdx = abs(nums[i]) - 1;
            if (nums[numIdx] < 0) {
                result.push_back(numIdx + 1);
            } else {
                nums[numIdx] = -nums[numIdx];
            }
        }
        return result;
    }
};