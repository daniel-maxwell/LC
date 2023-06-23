class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        set<int> range = {};
        set<int> numsSet = {};
        int count = 1;
        for (int n : nums) {
            range.insert(count);
            ++count;
            numsSet.insert(n);
        };
        nums = {};
        set_difference(range.begin(), range.end(), numsSet.begin(), numsSet.end(), std::inserter(nums, nums.end()));
        return nums;
    };
};