static const bool Init() {
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int l = 0, r = 0;
        int numNegatives = 0;
        int result = 0;
        while (r < nums.size()) {
            if (nums[l] == 0) {
                numNegatives = 0;
                ++l;
                r = l;
            }
            if (nums[r] == 0) {
                while (numNegatives % 2 != 0) {
                    if (nums[l] < 0) {
                        --numNegatives;
                    }
                    ++l;
                }
                if (nums[l] != 0) result = max(result, r - l);
                l = r + 1;
                r = l + 1;
                numNegatives = nums[l] < 0 ? 1 : 0;
                continue;
            } else if (nums[r] < 0) {
                ++numNegatives;
            }
            if (numNegatives % 2 == 0) {
                result = max(result, r - l + 1);
            }
            ++r;
        }

        while (numNegatives % 2 == 1) {
            if (nums[l] < 0) {
                --numNegatives;
                result = max(result, (r - (l + 1)));
            }
            ++l;
        }

        return result;
    }
};