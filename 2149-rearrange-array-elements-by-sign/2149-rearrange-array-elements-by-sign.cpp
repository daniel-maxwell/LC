auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int ptrA = 0;
        int ptrB = 1;
        while (!isOppositeSign(nums[ptrA], nums[ptrB])) ++ptrB;
        if (nums[ptrA] < 0) {
            int temp = ptrA;
            ptrA = ptrB;
            ptrB = temp;
        }
        int signA = nums[ptrA] < 0 ? -1 : 1;
        int signB = nums[ptrB] < 0 ? -1 : 1;

        vector<int> result(nums.size(), 0);
        int resIdx = 0;

        while (ptrA < nums.size() || ptrB < nums.size()) {
            if (ptrA < nums.size()) {
                result[resIdx] = nums[ptrA];
                ++resIdx;
                ++ptrA;
                while (ptrA < nums.size() && isOppositeSign(signA, nums[ptrA])) {
                    ++ptrA;
                }
            }
            if (ptrB < nums.size()) {
                result[resIdx] = nums[ptrB];
                ++resIdx;
                ++ptrB;
                while (ptrB < nums.size() && isOppositeSign(signB, nums[ptrB])) {
                    ++ptrB;
                }
            }
        }
        return result;
    }
    const bool isOppositeSign(const int a, const int b) {
        return (a >= 0 && b < 0) || (a < 0 && b >= 0);
    }
};