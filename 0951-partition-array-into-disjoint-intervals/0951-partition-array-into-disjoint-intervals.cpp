class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        
        vector<int> maximumLeft {nums[0]};
        vector<int> minimumRight(nums.size(), 0);
        minimumRight[minimumRight.size() - 1] = nums.back();

        int maxLeft = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            maxLeft = max(maxLeft, nums[i]);
            maximumLeft.push_back(maxLeft);
        }

        int minRight = nums.back();
        for (int i = nums.size() - 2; i >= 0; --i) {
            minRight = min(minRight, nums[i]);
            minimumRight[i] = minRight;
        }

        for (int i = 0; i < nums.size() - 1; ++i) {
            if (maximumLeft[i] <= minimumRight[i+1]) {
                return i + 1;
            }
        }

        return 0;
    }
};