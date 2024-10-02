static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int result = 0;
        if (goal == 0) {
            vector<int> setSizes;
            int l = 0, r = 1;
            int currSize = 1;
            while (l < nums.size()) {
                if (nums[l] == 1) {
                    ++l;
                    r = l;
                    currSize = 0;
                } else if (r >= nums.size() || nums[r] == 1) {
                    setSizes.push_back(currSize);
                    l = r + 1;
                    r = l;
                    currSize = 0;
                } else {
                    ++r;
                    ++currSize;
                }
            }
            for (const int &size : setSizes) {
                const double progSum = ((static_cast<double>(size) + 1) / 2) * size;
                result += static_cast<int>(progSum);
            }
            return result;
        } else {
            vector<int> oneIndices;
            for (int i = 0; i < nums.size(); ++i) {
                if (nums[i] == 1) { oneIndices.push_back(i); }
            }
            int l = 0, r = goal - 1;
            while (r < oneIndices.size()) {
                int leftZeroes = 0, rightZeroes = 0;
                int leftIdx = oneIndices[l] - 1, rightIdx = oneIndices[r] + 1;
                while (leftIdx >= 0 && nums[leftIdx] == 0) {
                    ++leftZeroes;
                    --leftIdx;
                }
                while (rightIdx < nums.size() && nums[rightIdx] == 0) {
                    ++rightZeroes;
                    ++rightIdx;
                }
                ++l;
                ++r;
                result += (leftZeroes + 1) * (rightZeroes + 1);
            }
            return result;
        }
        return 0;
    }
};