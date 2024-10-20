auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const void moveZeroes(vector<int>& nums) {
        int l = 0, r = 1;
        while (r < nums.size()) {
            if (r <= l) {r = l + 1; continue;}
            if (nums[r] == 0) {++r; continue;}
            if (nums[l] != 0) {++l; continue;}
            nums[l] = nums[r]; nums[r] = 0;
            ++l; ++r;
        }
    }
};