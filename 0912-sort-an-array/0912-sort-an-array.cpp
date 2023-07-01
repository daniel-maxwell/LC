class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
            if (nums.size() <= 1) return nums;
            vector<int> left (nums.begin(), nums.begin() + nums.size()/2);
            vector<int> right (nums.begin() + nums.size() / 2, nums.end());
            return merge(sortArray(left), sortArray(right));
        };

    vector<int> merge(vector<int>left, vector<int>right) {
        vector<int> result;
        auto left_it = left.begin();
        auto right_it = right.begin();

        while (left_it != left.end() && right_it != right.end()) {
            if (*left_it <= *right_it) {
                result.push_back(*left_it);
                ++left_it;
            }
            else {
                result.push_back(*right_it);
                ++right_it;
            };
        };

        if (left_it != left.end()) {
            result.insert(result.end(), left_it, left.end());
        }
        else {
            result.insert(result.end(), right_it, right.end());
        };
        return result;
    };
};