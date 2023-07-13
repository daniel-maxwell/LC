class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = floor((l + r) / 2);
            if (target < nums[mid]) r = --mid;
            else if (target > nums[mid]) l = ++mid;
            else return mid;
        };
        return l;
    };
};