class Solution {
public:
    const double minimumAverage(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        double minAvg = 51;
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            minAvg = min(minAvg, (double(nums[l]) + double(nums[r])) / 2);
            ++l;
            --r;
        }
        return minAvg;
    }
};