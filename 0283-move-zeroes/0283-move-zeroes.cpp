class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int idx = 0;

        // Move all the non-zero elements to the front
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[idx++] = nums[i];
            }
        }

        // Make all the remaining elements 0
        while (idx < n) {
            nums[idx++] = 0;
        }

    }
};