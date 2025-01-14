class Solution {
public:
    int thirdMax(const vector<int>& nums) {
        const unordered_set numSet (nums.begin(), nums.end());
        vector<int> nums2(numSet.begin(), numSet.end());
        sort(nums2.begin(), nums2.end());
        if (nums2.size() < 3) {
            return nums2.back();
        }
        return nums2[nums2.size()-3];
    }
};