class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count = {};
        vector<vector<int>> freq(nums.size() + 1);

        for (int n : nums) {
            if (count.find(n) != count.end()) ++count[n];
            else count[n] = 1;
        }

        for (auto const& entry : count) {
            freq[entry.second].push_back(entry.first);
        };

        vector<int> res = {};
        for (int j = 1; j < freq.size(); ++j) {
            for (int n = 0; n < freq[freq.size() - j].size(); ++n) {
                res.push_back(freq[freq.size() - j][n]);
                if (res.size() == k) {
                    return res;
                };
            };
        };
        return res;
    };
};