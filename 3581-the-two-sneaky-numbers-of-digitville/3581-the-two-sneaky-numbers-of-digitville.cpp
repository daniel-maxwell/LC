class Solution {
public:
    const vector<int> getSneakyNumbers(const vector<int>& nums) {

        unordered_set<int> digits;

        vector<int> result;

        for (const int &n : nums) {
            if (digits.contains(n)) {
                result.push_back(n);
            } else {
                digits.insert(n);
            }
        }

        return result;
    }
};