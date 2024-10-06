static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    const std::vector<std::vector<int>> findMatrix(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::set<int>> storage {{std::set<int>{}}};
        int prev = -1;
        for (const int &num : nums) {
            bool added = false;
            for (int i = 0; i < storage.size(); ++i) {
                if (!storage[i].contains(num)) {
                    storage[i].insert(num);
                    added = true;
                    break;
                }
            }
            if (!added) 
                storage.push_back(set<int>{num});
        }
        std::vector<std::vector<int>> result;
        for (const std::set<int> &s : storage)
            result.push_back(std::vector<int>(s.begin(), s.end()));
        return result;
    }
};