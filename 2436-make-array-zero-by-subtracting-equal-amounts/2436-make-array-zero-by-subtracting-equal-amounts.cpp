class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int subtractSum = 0;
        int result = 0;
        for (const int &n : nums) {
            if (subtractSum == n) {
                continue;
            } else {
                subtractSum += n - subtractSum;
                ++result;
            }
        }
        return result;
    }
};