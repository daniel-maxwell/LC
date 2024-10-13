auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long result = -1;
        long long sideSum = nums[0] + nums[1];
        for (int i = 2; i < nums.size(); ++i) {
            if (sideSum > nums[i]) {
                result = sideSum + nums[i];
            }
            sideSum += nums[i];
        }
        return result;
    }
};