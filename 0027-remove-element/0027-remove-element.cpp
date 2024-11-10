class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> nums2;
        int result = 0;
        for (const int & num: nums) {
            if (num != val) {
                nums2.push_back(num);
                ++result;
            }
        }
        nums = nums2;
        return result;
    }
};