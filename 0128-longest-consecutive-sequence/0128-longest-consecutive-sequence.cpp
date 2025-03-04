class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        unordered_set<int> numSet(nums.begin(), nums.end());
        int result = 0, i = 0;
        while (i < nums.size()) {
            if (!numSet.contains(nums[i])) {
                ++i;
                continue;
            }
            int increasing = 1, decreasing = 1;
            int curr = nums[i] + 1;
            while (numSet.contains(curr)) {
                numSet.erase(curr);
                ++increasing;
                ++curr;
            }
            curr = nums[i] - 1;
            while (numSet.contains(curr)) {
                numSet.erase(curr);
                ++decreasing;
                --curr;
            }
            result = max(result, increasing + decreasing - 1);
            ++i;
        }
        return result;
    }
};