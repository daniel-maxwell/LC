static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
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