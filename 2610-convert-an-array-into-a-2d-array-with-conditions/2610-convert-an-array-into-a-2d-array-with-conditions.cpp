static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    std::vector<std::vector<int>> findMatrix(std::vector<int>& nums) {
        std::map<int, int> counts;
        int maxCount = 0;

        for (const int &num : nums) {
            ++counts[num];
            if (counts[num] > maxCount) maxCount = counts[num];
        }
        
        std::vector<std::vector<int>> result(maxCount);
        
        for (const std::pair<int, int> &record : counts) {
            for (int i = 0; i < record.second; ++i) {
                result[i].push_back(record.first);
            }
        }
        return result;
    }
};