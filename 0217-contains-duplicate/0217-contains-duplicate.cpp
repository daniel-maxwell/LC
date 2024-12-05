class Solution {
public:
    const bool containsDuplicate(const vector<int>& nums) {
        unordered_set<int> numSet;
        for (const int &n : nums) {
            if (numSet.contains(n)) return true;
            numSet.insert(n);
        }
        return false;
    }
};