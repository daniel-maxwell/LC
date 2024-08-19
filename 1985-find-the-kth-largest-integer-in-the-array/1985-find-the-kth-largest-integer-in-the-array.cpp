class Solution {
public:
    string kthLargestNumber(vector<string>& nums, const int k) {
        sort(nums.begin(), nums.end(), [](const string &a, const string &b) {
            if (a.length() == b.length()) {
                return a < b;
            } else {
                return a.length() < b.length();
            }
        });
        return nums[nums.size() - k];
    }
};