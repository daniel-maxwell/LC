class Solution {
public:
    vector<int> majorityElement(vector<int> &nums) {
        const int threshold = nums.size() / 3;

        map<int, int> occurences{};

        for (int val : nums) {
            if (occurences.contains(val)) {
                occurences[val]++;
            } else {
                occurences[val] = 1;
            }
        }

        vector<int> result{};

        for (int val : nums) {
            if (occurences.contains(val) && occurences[val] > threshold) {
                result.push_back(val);
                occurences.erase(val);
            }
        }

        return result;
    }
};