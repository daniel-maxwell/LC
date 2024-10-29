auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int currNumIdx = 0;
        int x = 0;
        while (currNumIdx < nums.size()) {
            if (x > nums[currNumIdx]) {
                ++currNumIdx;
                continue;
            }
            if (x == nums.size() - currNumIdx) {
                return x;
            }
            ++x;
        }
        return -1;
    }
};