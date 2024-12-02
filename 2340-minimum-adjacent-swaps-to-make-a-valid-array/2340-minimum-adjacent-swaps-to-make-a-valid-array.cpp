class Solution {
public:
    int minimumSwaps(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        int minIdx = 0, minEl = nums[0], maxIdx = 0, maxEl = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] < minEl) {
                minIdx = i;
                minEl = nums[i];
            }
            if (nums[i] >= maxEl) {
                maxIdx = i;
                maxEl = nums[i];
            }
        }

        if (minIdx > maxIdx) {
            return minIdx + (nums.size() - (maxIdx + 2));
        } else {
            return minIdx + (nums.size() - (maxIdx + 1));
        }
    }
};