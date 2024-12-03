class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> uniqueNonZero;
        for (const int &num : nums) if (num > 0) uniqueNonZero.insert(num);
        return uniqueNonZero.size();
    }
};