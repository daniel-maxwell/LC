static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();

class Solution {
public:
    bool containsNearbyDuplicate(const vector<int>& nums, const int k) {
        map<int, vector<int>> valuesToIndices;

        for (int i = 0; i < nums.size(); ++i) {
            valuesToIndices[nums[i]].push_back(i);
        }

        for (auto &pair : valuesToIndices) {
            if (pair.second.size() < 2) continue;
            sort(pair.second.begin(), pair.second.end());
            for (int i = 0; i < pair.second.size() -1; ++i) {
                if (pair.second[i+1] - pair.second[i] <= k) {
                    return true;
                }
            }
        }

        return false;
    }
};