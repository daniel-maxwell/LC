class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        
        sort(nums.begin(), nums.end());

        bool hasZero = false;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                hasZero = true;
                break;
            }
            if (nums[i] > 0) {
                break;
            }
        }

        int i = 0;

        while (i < nums.size() && nums[i] < 0 && k > 0) {
            nums[i] = -nums[i];
            --k;
            ++i;
        }

        sort(nums.begin(), nums.end());

        if (!hasZero && k % 2 == 1) {
            nums[0] = -nums[0];
        }

        int result = 0;

        for (const int &n : nums) {
            result += n;
        }

        return result;
    }
};