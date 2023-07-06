class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + floor((r - l) / 2);
            if (target < nums[mid]) {
                r = --mid;
            }
            else if (target > nums[mid]) {
                l = ++mid;
            }
            else return mid;
        };
        return -1;
    };
};