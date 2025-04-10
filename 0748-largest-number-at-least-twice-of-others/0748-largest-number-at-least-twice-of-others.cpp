class Solution {
public:
    int dominantIndex(const vector<int>& nums) {
        int MAX = 0;
        int maxIdx = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > MAX) {
                maxIdx = i;
                MAX = nums[i];
            }
        }


        for (const int &n : nums) {
            if (n == MAX) continue;
            if (n * 2 > MAX) return -1;
        }

        return maxIdx;
    }
};